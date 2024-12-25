from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI, HTTPException, Query


app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (필요 시 특정 도메인으로 제한)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

# 파일 디렉토리 설정
FILES_DIR = "./services"

@app.get("/")
def read_root():
    return {"message": "FastAPI file server is running!", "files_directory": FILES_DIR}

@app.get("/files/{file_name}")
def get_file(file_name: str):
    """
    특정 파일을 제공하는 엔드포인트
    """
    file_path = os.path.join(FILES_DIR, file_name)

    # 파일 존재 여부 확인
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path)

@app.get("/files")
def list_files():
    """
    디렉토리 내 모든 파일 목록을 반환
    """
    try:
        files = os.listdir(FILES_DIR)
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading files: {e}")

