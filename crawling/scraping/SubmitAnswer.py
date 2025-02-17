from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import pickle
from dotenv import load_dotenv
from github.ConvertToGithubSearchFormat import convertToGithubSearchFormat
from github.GithubFindAnswer import findAnswerFromGithub
import time

# 쿠키 저장 함수
def save_cookies(driver, filename="cookies.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

# 쿠키 불러오기 함수
def load_cookies(driver, filename="cookies.pkl"):
    with open(filename, "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

# 쿠키 갱신 함수
def refresh_cookies(driver):
    # 쿠키를 다시 로드하고 로그인 절차를 통해 갱신
    login(driver)  # 로그인 함수 호출
    save_cookies(driver)  # 새 쿠키 저장

def tryCookieThenLogin(driver):
    """ ✅ 쿠키 로그인 시도 → 실패하면 새 로그인 """
    try:
        if login_using_cookies(driver):
            print("✅ 쿠키로 로그인 성공")
            return True
        elif login(driver):
            print("✅ 새로 로그인 성공")
            return True
        else:
            print("🚨 로그인 실패")
            return False

    except Exception as e:
        print(f"🚨 로그인 중 오류 발생: {e}")
        return False


def login(driver):
    driver.get("https://www.acmicpc.net/login")

    # 로그인 정보
    load_dotenv()
    username = os.getenv("BAEKJOON_USERNAME")
    password = os.getenv("BAEKJOON_PASSWORD")

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

        save_cookies(driver) #로그인 성공하고 쿠키 저장
        print("로그인 성공")
        return True

    except Exception as e:
        print(f"로그인 실패: {e}")
        return False

# 로그인 시 쿠키 사용 함수
def login_using_cookies(driver):
    driver.get("https://www.acmicpc.net")
    try:
        load_cookies(driver)  # 쿠키 불러오기
        driver.get("https://www.acmicpc.net/login")  # 페이지를 새로고침하여 로그인된 상태 확인
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "username"))
        )
        print("이미 로그인된 상태입니다.")
        return True
    except Exception as e:
        print(f"쿠키 로드 실패: {e}")
        return False

# 백준에 정답을 제출하는 코드
def setup_driver():
    #     options = Options()
    #     options.add_argument("--headless")  # 필요에 따라 주석 처리
    #     return webdriver.Chrome(options=options)
    return webdriver.Chrome()

def submit_code(driver, problem_id, language, source_code):
    driver.get(f'https://www.acmicpc.net/submit/{problem_id}')

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "CodeMirror"))
        )

        driver.execute_script("""
        var editor = document.querySelector('.CodeMirror').CodeMirror;
        editor.setValue(arguments[0]);
        """, source_code)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'language_chosen')))
        driver.execute_script('$("#language_chosen").trigger("mousedown");')
        langs = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.chosen-results li')))

        lang_selected = False
        for lang in langs:
            # print("1. :", lang.text.lower())
            # print("2. :", language.lower())
            if lang.text.lower() == language.lower():
                lang.click()
                lang_selected = True
                break

        if not lang_selected:
            print("선택한 언어를 찾을 수 없습니다.")
            return False

        submit_button = driver.find_element(By.ID, "submit_button")
        submit_button.click()

        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#status-table tbody tr:first-child .result-text')))
        print(f"제출 결과: {result.text}")

        result_wait_status = ["기다리는 중", "채점 준비 중", "재채점을 기다리는 중", "채점 중"]
        result_finish_status = ["맞았습니다!!", "출력 형식이 잘못되었습니다", "틀렸습니다", "시간 초과", "메모리 초과", "출력 초과", "런타임 에러", "컴파일 에러"]


        while True:
            print("🔄 채점 진행 중...")
            time.sleep(1) # ✅ 1초 대기 후 다시 확인

            result = driver.find_element(By.CSS_SELECTOR, '#status-table tbody tr:first-child .result-text')

            # ✅ "채점 중 (2%)" 과 같은 형식도 확인 (정규 표현식 사용)
            if result.text in result_finish_status:
                break  # ✅ 채점 완료 상태라면 반복문 종료

        return '점' in result.text or '맞았습니다' in result.text

    except TimeoutException:
        print("제출 실패: 페이지 로딩 시간 초과")
        return False
    except NoSuchElementException as e:
        print(f"제출 실패: 요소를 찾을 수 없습니다. {e}")
        return False
    except Exception as e:
        print(f"제출 중 오류 발생: {e}")
        return False

if __name__ == "__main__":

    problem_id = "1027"

    searchFormat = convertToGithubSearchFormat(problem_id)
    code, submitLang = findAnswerFromGithub(searchFormat)
