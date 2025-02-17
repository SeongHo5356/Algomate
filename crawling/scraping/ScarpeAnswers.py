from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from dotenv import load_dotenv
from CheckServerSolved import check_problem_solved

from github.ConvertToGithubSearchFormat import convertToGithubSearchFormat
from github.GithubFindAnswer import findAnswerFromGithub
from utils.mime_utils import get_file_extension_and_folder
from SubmitAnswer import login, login_and_submit_code

import os



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

# ✅ 1. 코드 링크 크롤링 함수
def get_solution_links(driver, base_url, page=1):
    """ 특정 문제의 정답 코드 페이지에서 코드 링크 가져오기 """
    driver.get(base_url + str(page))
    time.sleep(1)  # 과도한 요청 방지

    try:
        code_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/source/"]'))
        )
        return code_links
    except TimeoutException:
        print(f"{page} 페이지에서 코드 링크를 찾을 수 없습니다.")
        return []

# ✅ 2. 코드 페이지에서 코드 내용 크롤링 함수
def extract_solution_details(driver):
    """ 개별 코드 페이지에서 유저 아이디, 코드 내용, 언어 정보 가져오기 """
    try:
        user_id_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr td a[href^='/user/']"))
        )
        user_id = user_id_element.text

        code_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='source']"))
        )
        code_text = code_element.get_attribute("value")
        mime_type = code_element.get_attribute("data-mime")

        return user_id, code_text, mime_type
    except TimeoutException:
        print("코드 정보를 가져오지 못했습니다.")
        return None, None, None

# ✅ 3. 코드 크롤링 (파일 저장 X, API 전송 X)
def scrape_solutions(driver, problem_id, language_id):
    """
    특정 문제의 정답 코드들을 크롤링하여 리스트로 반환 (파일 저장 X, API 전송 X)

    Returns:
        list(dict): 크롤링한 코드 데이터 리스트
    """
    base_url = f"https://www.acmicpc.net/problem/status/{problem_id}/{language_id}/"
    solutions = []  # 메모리 내 리스트

    for page in range(1, 2):  # 현재 1페이지만 크롤링
        code_links = get_solution_links(driver, base_url, page)

        print(code_links)

        for i in range(len(code_links)):
            try:
                code_links = get_solution_links(driver, base_url, page)  # 요소 새로고침
                code_links[i].click()  # 코드 페이지 이동
                time.sleep(1)

                user_id, code_text, mime_type = extract_solution_details(driver)
                if not user_id or not code_text:
                    driver.back()
                    continue

                solutions.append({
                    "user_id": user_id,
                    "code": code_text,
                    "mime_type": mime_type
                })

                driver.back()
                time.sleep(1)
            except StaleElementReferenceException:
                print("StaleElementReferenceException 발생, 다음 코드로 넘어갑니다.")
                continue

    print(solutions)

    return solutions


# ✅ 4. 파일 저장 함수
def save_solution_to_file(problem_id, user_id, code_text, mime_type, base_save_directory="solutions"):
    """ 크롤링한 코드를 파일로 저장하는 함수 """
    file_extension, language_folder = get_file_extension_and_folder(mime_type)

    # 디렉토리 설정
    base_problem_directory = os.path.join(base_save_directory, str(problem_id), language_folder)
    os.makedirs(base_problem_directory, exist_ok=True)

    # 파일 저장
    filename = f"{user_id}.{file_extension}"
    file_path = os.path.join(base_problem_directory, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(code_text)

    print(f"코드 저장 완료: {file_path}")
    return file_path, file_extension

# ✅ 5. API 전송 함수
def send_solution_to_api(problem_id, file_path, file_extension, user_id):
    """ API로 솔루션 전송 """
    # 여기에 db_controller API 호출 로직 추가
    print(f"API 전송: 문제 {problem_id}, 파일 {file_path}, 유저 {user_id}")


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


# ✅ 9. 최종 실행 함수 (로그인, 크롤링, 저장, 전송)
def full_scrape_process(driver, problem_id, language_id):

    solutions = scrape_solutions(driver, problem_id, language_id)

    # 크롤링한 코드 저장
    for solution in solutions:
        file_path, file_extension = save_solution_to_file(problem_id, solution["user_id"], solution["code"], solution["mime_type"])
        # API로 전송
        send_solution_to_api(problem_id, file_path, file_extension, solution["user_id"])

# 메인 코드
if __name__ == "__main__":

    # WebDriver 설정
    driver = webdriver.Chrome()  # 크롬 드라이버 경로를 환경 변수에 추가했거나, 직접 지정해야 합니다.
    load_dotenv()

    problem_id = "1027"

    searchFormat = convertToGithubSearchFormat(problem_id)
    code, submitLang = findAnswerFromGithub(searchFormat)

    if code:
        success = login_and_submit_code(driver, problem_id, submitLang, code)
        print(f"제출 성공: {success}")
    else:
        print("코드를 가져오는데 실패했습니다.")


    full_scrape_process(driver, problem_id, "1003")
    #    pretty_print_solutions(solutions)

    #         # 출력
    #         for idx, solution in enumerate(solutions, 1):
    #             print(f"코드 {idx}:\n{solution}\n{'='*40}\n")

    # WebDriver 종료
    driver.quit()
