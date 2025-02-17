import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# ✅ Redis를 Celery의 브로커(Broker)로 설정
CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery("tasks", broker=CELERY_BROKER_URL)

celery_app.conf.update(
    result_backend=CELERY_BROKER_URL,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Seoul",
)
