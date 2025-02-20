from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from workers.scraping_tasks import scrape_baekjoon
from celery.result import AsyncResult
from config.CeleryConfig import celery_app

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


@router.get("/task-status/{task_id}")
def get_task_status(task_id: str):
    """ ✅ Celery 작업 상태 조회 API - Redis에서 직접 데이터 가져오기 """
    result = AsyncResult(task_id, app=celery_app)

    # ✅ 백엔드에서 직접 데이터 가져오기
    task_meta = result.backend.get_task_meta(task_id)

    return {
        "task_id": task_id,
        "status": task_meta.get("status"),  # PENDING, STARTED, SUCCESS, FAILURE 등
        "result": task_meta.get("result"),  # 작업 결과
        "date_done": task_meta.get("date_done"),  # 완료 시간
    }
