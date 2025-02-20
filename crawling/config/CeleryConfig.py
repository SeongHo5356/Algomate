import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# ✅ Redis 컨테이너 이름과 일치하도록 수정
# BROKER_URL = "redis://localhost:6379/0"
# BACKEND_URL = "redis://localhost:6379/0"

BROKER_URL = os.getenv("CELERY_BROKER_URL")
BACKEND_URL = os.getenv("CELERY_RESULT_BACKEND")

# ✅ Redis 설정 (Celery와 연동)
celery_app = Celery(
    "scraper",
    broker=BROKER_URL, # 🔹 메시지 브로커 (현재 Redis 사용 중)
    backend=BACKEND_URL, # 🔹 작업 결과 저장을 위한 백엔드 추가
    include=["workers.scraping_tasks"]
)

celery_app.conf.update(
    task_track_started=True,
    task_ignore_result=False,  # 🔹 결과를 무시하지 않도록 설정
    result_expires=360,  # 🔹 작업 결과를 6분 동안 유지
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Seoul",
    enable_utc=True,
)
