from github.ConvertToGithubSearchFormat import convertToGithubSearchFormat
from github.GithubFindAnswer import findAnswerFromGithub
from scraping.CheckServerSolved import check_problem_solved
from scraping.SubmitAnswer import login_using_cookies, login, submit_code, tryCookieThenLogin
from dotenv import load_dotenv
from selenium import webdriver

class ScrapingService:

    @staticmethod
    # 쿠키로 로그인해보고 안되면 새로 로그인 그리고 정답을 제출
    def login_and_submit_code(driver, problem_id, language, code):
        try:
            if login_using_cookies(driver):
                print("✅ 쿠키로 로그인 성공")
            else:
                if login(driver):
                    print("✅ 새로 로그인 성공")

            return submit_code(driver, problem_id, language, code)

        except Exception as e:
            print(f"🚨 로그인 및 제출 중 오류 발생: {e}")
            return False

    @staticmethod
    def scrapeWhenServerNotSolved(driver, problem_id, language_id):
        """ ✅ 맞춘 적 없는 문제일 때  -> 제출 -> 크롤링 """
        from scraping.ScarpeAnswers import scrape_solutions, save_solution_to_file, send_solution_to_api

        load_dotenv()

        searchFormat = convertToGithubSearchFormat(problem_id)
        code, submitLang = findAnswerFromGithub(searchFormat)

        if code:
            # ✅ 1. 로그인 & 정답 제출
            success = ScrapingService.login_and_submit_code(driver, problem_id, submitLang, code)
            print(f"✅ 제출 성공 여부: {success}")

        else:
            print("코드를 가져오는데 실패했습니다.")



        # ✅ 2. 정답 코드 크롤링 진행 (같은 WebDriver 사용)
        solutions = scrape_solutions(driver, problem_id, language_id)

        # ✅ 3. 크롤링한 코드 저장 및 API 전송
        for solution in solutions:
            # file_path, file_extension = save_solution_to_file(
            #     problem_id, solution["user_id"], solution["code"], solution["mime_type"]
            # )
            send_solution_to_api(problem_id, solution["user_id"], solution["code"], solution["mime_type"])

        print("✅ 전체 크롤링 및 저장 완료!")

    @staticmethod
    def scrapeWhenServerSolved(driver, problem_id, language_id):
        """ 이미 맞춘 적 있는 문제일 때 -> 바로 크롤링 """
        from scraping.ScarpeAnswers import scrape_solutions, send_solution_to_api

        # ✅ 1. 로그인 & 정답 제출
        success = tryCookieThenLogin(driver)
        print(f"✅ 로그인: {success}")

        # ✅ 2. 정답 코드 크롤링 진행 (같은 WebDriver 사용)
        solutions = scrape_solutions(driver, problem_id, language_id)

        # ✅ 3. 크롤링한 코드 저장 및 API 전송
        for solution in solutions:
            # file_path, file_extension = save_solution_to_file(
            #     problem_id, solution["user_id"], solution["code"], solution["mime_type"]
            # )
            send_solution_to_api(problem_id, solution["user_id"], solution["code"], solution["mime_type"])

        print("✅ 전체 크롤링 및 저장 완료!")

    @staticmethod
    def fullScrapeProcess(driver, problem_id, language_id):
        solvedStatus = check_problem_solved(problem_id)

        if solvedStatus:
            print("✅ 해당 문제 푼적 있음")
            ScrapingService.scrapeWhenServerSolved(driver, problem_id, language_id)
        else :
            print("🚨 해당 문제 푼적 없음")
            ScrapingService.scrapeWhenServerNotSolved(driver, problem_id, language_id)


if __name__ == "__main__":
    driver = webdriver.Chrome()

    load_dotenv()

    try:
        # ✅ 크롤링 실행 (문제 ID와 언어 ID 설정)
        problem_id = "1030"
        language_id = "1003"  # 예시 언어 ID

        print("🚀 크롤링 프로세스 시작...")
        ScrapingService.fullScrapeProcess(driver, problem_id, language_id)
        print("✅ 크롤링 완료!")

    finally:
        driver.quit()  # ✅ WebDriver 종료