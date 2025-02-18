import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# ✅ Redis 컨테이너 이름과 일치하도록 수정
BROKER_URL = "redis://localhost:6379/0"
BACKEND_URL = "redis://localhost:6379/0"


celery_app = Celery(
    "scraper",
    broker=BROKER_URL,
    backend=BACKEND_URL,
    include=["workers.scraping_tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Seoul",
    enable_utc=True,
)
