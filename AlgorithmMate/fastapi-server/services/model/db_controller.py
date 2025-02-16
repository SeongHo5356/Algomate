import requests

# 포스트 요청을 보내서 db에 저장
def send_solution_to_api(problem_id, file_path, language, user_id):
    url = "http://localhost:8080//api/v1/solution/save"
    payload = {
        "problemId": problem_id,
        "filePath": file_path,
        "language": language,
        "userId": user_id
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("데이터 저장 성공")
    else:
        print("데이터 저장 실패:", response.text)
