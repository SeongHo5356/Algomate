from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.scraping_service import ScrapingService
from selenium import webdriver
from dotenv import load_dotenv

router = APIRouter()

class ScrapeRequest(BaseModel):
    problem_id: str
    language_id: str


@router.post("/scrape")
async def start_scraping(request: ScrapeRequest):
    """
    ✅ 백준 문제 크롤링 및 정답 수집 API
    """
    load_dotenv()

    try:
        driver = webdriver.Chrome()  # 크롬 드라이버 실행
        ScrapingService.fullScrapeProcess(driver, request.problem_id, request.language_id)
        driver.quit()  # 크롤링 후 드라이버 종료
        return {"message": "✅ 크롤링 완료", "problem_id": request.problem_id}

    except Exception as e:
        driver.quit()  # 에러 발생 시 드라이버 종료
        raise HTTPException(status_code=500, detail=f"🚨 크롤링 중 오류 발생: {str(e)}")
