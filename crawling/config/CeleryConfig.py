from celery import Celery

celery = Celery(
    "scraping",
    broker = "redis://127.0.0.1:6379/0", # Redis를 브로커로 사용
    backend = "redis://127.0.0.1:6379/0", # 작업 결과 저장
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Seoul",
    enable_utc=True,
)
