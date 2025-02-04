from selenium import webdriver
import json
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from dotenv import load_dotenv
from check_server_solved import check_problem_solved
from full_process_search_n_submit import f_process
from language_options import get_file_extention_and_folder


# 로그인 함수
def login(driver, username, password):
    driver.get("https://www.acmicpc.net/login")

    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "login_user_id"))
        )
        username_field.send_keys(username)

        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "login_password"))
        )
        password_field.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit_button"))
        )
        login_button.click()

        # Check for reCAPTCHA
        try:
            recaptcha_frame = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
            print("reCAPTCHA detected. Please solve it manually.")
            WebDriverWait(driver, 120).until(
                EC.invisibility_of_element_located((By.XPATH, "//iframe[contains(@src, 'recaptcha')]"))
            )
        except NoSuchElementException:
            pass  # No reCAPTCHA detected

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "username"))
        )
        print("로그인 성공")
        return True
    except TimeoutException:
        print("로그인 실패: 요소를 찾을 수 없거나 클릭할 수 없습니다.")
        return False


# 페이지 수 확인 함수
def get_max_pages(driver, base_url):
    driver.get(base_url + "/1")
    time.sleep(1)
    print("start")
    try:
        # 페이지 번호 링크들 찾기
        page_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.pagination a'))
        )

        # 각 페이지 버튼의 텍스트를 숫자로 변환하고 가장 큰 값을 찾음
        page_numbers = [
            int(button.text) for button in page_buttons if button.text.isdigit()
        ]

        print("page_numbers : ", page_numbers)
        if page_numbers:
            return max(page_numbers)  # 가장 큰 페이지 번호 반환
        else:
            print(1)
            return 1  # 페이지 네비게이션이 없으면 1페이지만 존재
    except TimeoutException:
        print("TimeoutException")
        return 1



# 정답 코드 크롤링 및 파일 저장 함수
def scrape_solutions(driver, problem_id, language_id, base_save_directory="solutions"):
    base_url = f"https://www.acmicpc.net/problem/status/{problem_id}/{language_id}/"
    max_pages = get_max_pages(driver, base_url)

    ## 정답을 맞춘 적 없을 때
    if (check_problem_solved(problem_id) == False):
        print ("정답을 맞춘적 없음")
        f_process(problem_id)
        driver.refresh()

        # 저장 디렉토리 생성 (문제 번호 기준)
        base_problem_directory = os.path.join(base_save_directory, str(problem_id))
        if not os.path.exists(base_problem_directory):
            os.makedirs(base_problem_directory)

        solutions = []  # 메모리에 저장할 리스트
        solution_count = 1

        # for page in range(1, max_pages + 1):
        for page in range(1,2):
            driver.get(base_url + str(page))
            time.sleep(1)  # 사이트에 과도한 요청을 피하기 위해 잠시 대기

            try:
                # 코드 링크 요소 가져오기
                code_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/source/"]'))
                )

                # 각 링크를 개별적으로 접근하여 새롭게 요소를 가져옵니다
                for i in range(len(code_links)):
                    code_links = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/source/"]'))
                    )  # 페이지로 돌아온 후 다시 요소 목록을 가져옴

                    try:
                        code_links[i].click()  # 코드 링크 클릭
                        time.sleep(1)

                        user_id_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr td a[href^='/user/']"))
                        )
                        # 아이디 텍스트 가져오기
                        user_id = user_id_element.text
                        print(f"해당코드의 제출자: {user_id}")


                        # 코드 내용과 언어 정보 가져오기
                        code_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='source']"))
                        )
                        code_text = code_element.get_attribute("value")

                        # 언어에 따른 파일 확장자 및 디렉토리 설정
                        mime_type = code_element.get_attribute("data-mime")
                        file_extension, language_folder = get_file_extention_and_folder(mime_type)

                        # 언어별 저장 디렉토리 생성
                        language_directory = os.path.join(base_problem_directory, language_folder)
                        if not os.path.exists(language_directory):
                            os.makedirs(language_directory)

                        # 파일명 설정 및 저장
                        filename = f"{user_id}.{file_extension}"
                        file_path = os.path.join(language_directory, filename)

                        with open(file_path, "w", encoding="utf-8") as file:
                            file.write(code_text)

                        print(f"코드 {solution_count} 저장 완료: {file_path}")

                        # 메모리 내 리스트에도 저장
                        solutions.append({
                            "code": code_text,
                            "file_path": file_path,
                            "language": file_extension
                        })
                        solution_count += 1

                        # 뒤로가기
                        driver.back()
                        time.sleep(1)

                    except StaleElementReferenceException:
                        print("StaleElementReferenceException: 페이지 요소가 유효하지 않습니다.")
                        continue  # 현재 요소가 유효하지 않은 경우 건너뜀

            except TimeoutException:
                print(f"{page} 페이지에서 코드 링크를 찾을 수 없습니다.")
                break

    ## 정답을 맞췄을 때
    else:
        # 저장 디렉토리 생성 (문제 번호 기준)
        base_problem_directory = os.path.join(base_save_directory, str(problem_id))
        if not os.path.exists(base_problem_directory):
            os.makedirs(base_problem_directory)

        solutions = []  # 메모리에 저장할 리스트
        solution_count = 1

        # for page in range(1, max_pages + 1):
        for page in range(1, 2):
            driver.get(base_url + str(page))
            time.sleep(1)  # 사이트에 과도한 요청을 피하기 위해 잠시 대기

            try:

                # 코드 링크 요소 가져오기
                code_links = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/source/"]'))
                )

                # 각 링크를 개별적으로 접근하여 새롭게 요소를 가져옵니다
                for i in range(len(code_links)):
                    code_links = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/source/"]'))
                    )  # 페이지로 돌아온 후 다시 요소 목록을 가져옴

                    try:
                        code_links[i].click()  # 코드 링크 클릭
                        time.sleep(1)

                        # 제출 아이디 크롤링
                        user_id_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr td a[href^='/user/']"))
                        )
                        # 아이디 텍스트 가져오기
                        user_id = user_id_element.text
                        print(f"해당코드의 제출자: {user_id}")

                        # 코드 내용과 언어 정보 가져오기
                        code_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='source']"))
                        )
                        code_text = code_element.get_attribute("value")

                        # 언어에 따른 파일 확장자 및 디렉토리 설정
                        mime_type = code_element.get_attribute("data-mime")
                        file_extension, language_folder = get_file_extention_and_folder(mime_type)

                        # 언어별 저장 디렉토리 생성
                        language_directory = os.path.join(base_problem_directory, language_folder)
                        if not os.path.exists(language_directory):
                            os.makedirs(language_directory)

                        # 파일명 설정 및 저장
                        filename = f"{user_id}.{file_extension}"
                        file_path = os.path.join(language_directory, filename)

                        with open(file_path, "w", encoding="utf-8") as file:
                            file.write(code_text)

                        print(f"코드 {solution_count} 저장 완료: {file_path}")

                        # 메모리 내 리스트에도 저장
                        solutions.append({
                            "code": code_text,
                            "file_path": file_path,
                            "language": file_extension
                        })
                        solution_count += 1

                        # 뒤로가기
                        driver.back()
                        time.sleep(1)

                    except StaleElementReferenceException:
                        print("StaleElementReferenceException: 페이지 요소가 유효하지 않습니다.")
                        continue  # 현재 요소가 유효하지 않은 경우 건너뜀

            except TimeoutException:
                print(f"{page} 페이지에서 코드 링크를 찾을 수 없습니다.")
                break

    return solutions


def get_language_details(mime_type):
    """
    MIME 타입을 기반으로 파일 확장자와 언어 폴더를 반환합니다.

    Args:
        mime_type (str): MIME 타입 문자열.

    Returns:
        tuple: (파일 확장자, 언어 폴더 이름)
    """
    language_map = {
        "c++": ("cpp", "cpp"),
        "python": ("py", "python"),
        "java": ("java", "java"),
        "c": ("c", "c"),
    }

    for key, value in language_map.items():
        if key in mime_type:
            return value

    return "txt", "other"  # 기본 파일 확장자와 폴더



# 각 코드 블록을 보기 좋게 출력하는 함수
def pretty_print_solutions(solutions):
    for idx, solution in enumerate(solutions, 1):
        code_text = solution['code']
        file_path = solution['file_path']
        language = solution['language']

        print(f"코드 {idx}:")
        print(f"파일 경로: {file_path}")
        print(f"언어: {language}")
        print("=" * 40)
        print(code_text)  # 코드 본문
        print("=" * 40, end="\n\n")


# 메인 코드
if __name__ == "__main__":
    # WebDriver 설정
    driver = webdriver.Chrome()  # 크롬 드라이버 경로를 환경 변수에 추가했거나, 직접 지정해야 합니다.

    load_dotenv()
    username = os.getenv("BAEKJOON_USERNAME")
    password = os.getenv("BAEKJOON_PASSWORD")

    print(username)
    print(password)
    # 로그인
    if login(driver, username, password):
        # 특정 문제와 언어의 정답 코드 가져오기
        problem_id = "1027" #input("문제번호를 입력해주세요 : ")  # 문제 ID
        language_id = '1003'  # 언어 ID (Python 3)

        solutions = scrape_solutions(driver, problem_id, language_id)

    #    pretty_print_solutions(solutions)

    #         # 출력
    #         for idx, solution in enumerate(solutions, 1):
    #             print(f"코드 {idx}:\n{solution}\n{'='*40}\n")

    # WebDriver 종료
    driver.quit()
