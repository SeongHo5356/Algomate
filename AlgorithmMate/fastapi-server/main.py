from fastapi import HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from services import check_server_solved
from services.check_code_similarity import run_jplag
from services.language_options import map_language_to_jplag_option, map_language_to_file_extension, \
    get_folder_from_extension
# from services.save_file_to_client import save_top_similarity_files
import uvicorn
from fastapi import FastAPI
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


from fastapi.responses import FileResponse

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 필요한 도메인을 명시하거나 '*'로 모든 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

@app.get("/api/problem/{problem_id}/solved_status")
def check_problem_solved_status(username: str, problem_id: int):
    problem_status = check_server_solved.get_all_problems(username)
    if problem_status is None:
        raise HTTPException(status_code=404, detail="User not found or page unavailable")
    if problem_id in problem_status["solved"]:
        return {"status": "solved"}
    elif problem_id in problem_status["partially_solved"]:
        return {"status": "partially solved"}
    elif problem_id in problem_status["attempted_but_not_solved"]:
        return {"status": "attempted but not solved"}
    else:
        return {"status": "not attempted"}


class CodeData(BaseModel):
    code: str
    problem_id : str
    userId: str = None
    language: str

@app.post("/submit-code")
async def receive_code(data: CodeData):
    data.problem_id = data.problem_id.split('번')[0]
    try:
        # 제출된 코드를 처리하거나 저장하는 로직
        print(f"Code :\n{data.code}")
        print(f"User ID: {data.userId}")
        print(f"Problem Number: {data.problem_id}")
        print(f"language: {data.language}")
        # 문제 번호와 유저 ID를 사용해 폴더 및 파일 저장 경로 생성
        problem_number = data.problem_id  # 실제로 문제 번호를 받을 수 있도록 수정 필요
        base_directory = "services/solutions"
        user_directory = os.path.join(base_directory, problem_number)

        # 언어 태그 매핑
        jplag_language = map_language_to_jplag_option(data.language)
        # 파일 확장자 결정
        file_extension = map_language_to_file_extension(data.language)
        print("file_extension: ", file_extension)
        folder_name = get_folder_from_extension(str(data.language))
        print("folder_name: ", folder_name)

        if not os.path.exists(user_directory):
            os.makedirs(user_directory)

        # 파일명은 유저 ID로 설정
        filename = f"{data.userId}{file_extension}" if data.userId else f"submission{file_extension}"
        file_path = os.path.join(user_directory, folder_name, filename)
        print("file_path: ", file_path)

        # 파일에 코드 저장
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data.code)

        print(f"Code saved to {file_path}")

        jplag_path = "C:/Users/kjeng/Desktop/jplag_3_0.jar"
        solutions_path = "C:/Users/kjeng/Desktop/Study/Algomate/Algomate/AlgorithmMate/fastapi-server/services/solutions/"+str(problem_number)+"/"+str(folder_name)
        results_path = "C:/Users/kjeng/Desktop/Study/Algomate/Algomate/AlgorithmMate/fastapi-server/services/solutions/"+str(problem_number)+"/"+str(folder_name)+"/result"
        to_clients_path = "C:/Users/kjeng/Desktop/Study/Algomate/Algomate/AlgorithmMate/fastapi-server/services/toClients"

        # JPlag 실행 및 유사도 결과 가져오기
        similarity_results = run_jplag(jplag_path, solutions_path, results_path, language=jplag_language, keyword = data.userId)

        # 상위 2개의 유사도 결과 파일 저장
        # similarities = save_top_similarity_files(similarity_results, solutions_path, to_clients_path, keyword = data.userId)
        # print(similarities)

        # JPlag 실행 후 저장된 파일 삭제
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted the file: {file_path}")
            except OSError as e:
                print(f"Error deleting file {file_path}: {e}")
        else:
            print(f"File does not exist: {file_path}")

        return {"status": "success", "message": "Code data received and saved", "similarities": similarities}


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class PageData(BaseModel):
    title: str
    content: str
    userId: Optional[str] = None  # Optional로 설정하여 userId가 없을 때에도 처리 가능

@app.post("/submit-data")
async def receive_data(data: PageData):
    data.title = data.title.split('번')[0]
    try:
        # 받은 데이터 출력 또는 저장
        print(f"문제번호 : {data.title}")
        if data.userId:
            print(f"User ID: {data.userId}")
        else :
            print("로그인되지 않음") # data.content[:4] == "회원가입", userId = data.content[:15].split("설정")[0]

        return {"message": "Data received successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




# 파일 디렉토리 설정
FILES_DIR = "./services/toClients"

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

# 변경된 파일 목록 저장
modified_files = []

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global modified_files
        if event.is_directory:
            return
        # 변경된 파일의 경로 추가
        modified_files.append(event.src_path)
        print(f"파일 변경 감지: {event.src_path}")

    def on_created(self, event):
        # 파일 생성 처리
        print(f"파일 생성 감지: {event.src_path}")

    def on_deleted(self, event):
        # 파일 삭제 처리
        print(f"파일 삭제 감지: {event.src_path}")

# FastAPI 엔드포인트
@app.get("/modified-files")
def get_modified_files():
    global modified_files
    # 현재까지 감지된 변경된 파일 반환
    return {"modified_files": modified_files}

from services.model.models import SessionLocal
from services.model.db_service import add_solution_to_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, Query

# 의존성 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic 모델을 사용하여 데이터를 받음
class SolutionIn(BaseModel):
    problem_id: str
    file_path: str
    language: str
    user_id: str

@app.post("/solutions")
async def save_solution(
    solution: SolutionIn,  # Body로 받기
    db: Session = Depends(get_db)
):
    add_solution_to_db(db, solution.problem_id, solution.file_path, solution.language, solution.user_id)
    return {"message": "Solution saved successfully"}

if __name__ == "__main__":
    # 파일 감지 설정
    directory_to_watch = "./services"
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_watch, recursive=True)
    observer.start()


    try:
        print("FastAPI 서버 시작 중...")
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()