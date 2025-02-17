from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from workers.scraping_tasks import scrape_baekjoon

router = APIRouter()

class ScrapeRequest(BaseModel):
    problem_id: str
    language_id: str

@router.post("/scrape")
async def start_scraping(request: ScrapeRequest):
    """
    ✅ 크롤링을 Celery 비동기 작업으로 실행
    """
    task = scrape_baekjoon.delay(request.problem_id, request.language_id)  # ✅ 비동기 실행
    return {"message": "✅ 크롤링 작업이 시작되었습니다.", "task_id": task.id}