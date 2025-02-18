from fastapi import FastAPI
from controllers.scraping_controller import router as scraping_router

app = FastAPI(title="Baekjoon Scraper API")

# ✅ 컨트롤러 등록
app.include_router(scraping_router, prefix="/api", tags=["Scraping"])

@app.get("/")
def read_root():
    return {"message": "✅ FastAPI 서버 실행 중"}