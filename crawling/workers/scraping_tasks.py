from config.CeleryConfig import celery_app
from services.scraping_service import ScrapingService
from dotenv import load_dotenv
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import tempfile
import uuid
import time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ 환경 변수 로드 (한 번만)
load_dotenv()

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ✅ GUI 없이 실행
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_extension("/app/crx/auto_recaptcha_solver.crx")
    chrome_options.add_extension("/app/crx/recaptcha_autoclick.crx")
    # User-Agent 설정 (일반적인 브라우저로 설정)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

    # ✅ Chromedriver 경로 명확하게 지정
    chromedriver_path = "/usr/bin/chromedriver"
    service = Service(chromedriver_path)

    return webdriver.Chrome(service=service, options=chrome_options)

@celery_app.task(name="scrape_baekjoon")
def scrape_baekjoon(problem_id, language_id):
    """ ✅ 백준 크롤링을 백그라운드에서 실행하는 Celery Task """
    driver = None  # ✅ 예외 발생 시에도 driver.quit()을 호출하기 위해 선언

    try:
        logger.info(f"🚀 크롤링 시작: 문제 ID={problem_id}, 언어 ID={language_id}")

        driver = get_driver()
        print(1)
        ScrapingService.fullScrapeProcess(driver, problem_id, language_id)

        logger.info(f"✅ 크롤링 완료: 문제 ID={problem_id}")
        return {"message": "✅ 크롤링 완료", "problem_id": problem_id}

    except Exception as e:
        logger.error(f"🚨 크롤링 중 오류 발생: {str(e)}", exc_info=True)
        return {"error": f"🚨 크롤링 중 오류 발생: {str(e)}"}

    finally:
        if driver:
            driver.quit()
            logger.info("🛑 WebDriver 종료 완료")


