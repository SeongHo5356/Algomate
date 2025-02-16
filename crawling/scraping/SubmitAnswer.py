from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os
from dotenv import load_dotenv
from github.ConvertToGithubSearchFormat import get_problem_info
from github.GithubFindAnswer import findAnswerFromGithub

# 백준에 정답을 제출하는 코드
def setup_driver():
    #     options = Options()
    #     options.add_argument("--headless")  # 필요에 따라 주석 처리
    #     return webdriver.Chrome(options=options)
    return webdriver.Chrome()


def login(driver):
    driver.get("https://www.acmicpc.net/login")

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
        print("로그인 성공")
        return True

    except TimeoutException:
        print("로그인 실패: 요소를 찾을 수 없거나 클릭할 수 없습니다.")
        return False


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


def login_and_submit_code(problem_id, language, code):
    driver = setup_driver()
    try:
        if login(driver):
            return submit_code(driver, problem_id, language, code)
        return False
    finally:
        driver.quit()


if __name__ == "__main__":
    load_dotenv()

    github_token = os.getenv("API_TOKEN")

    problem_id = "16144"
    language = "C++17"

    query = get_problem_info(problem_id)
    code = findAnswerFromGithub(query, github_token)

    if code:
        success = login_and_submit_code(problem_id, language, code)
        print(f"제출 성공: {success}")
    else:
        print("코드를 가져오는데 실패했습니다.")