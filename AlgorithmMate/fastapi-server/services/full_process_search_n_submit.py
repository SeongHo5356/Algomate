import os
from dotenv import load_dotenv

from baekjoon_find_answer import main
from baekjoon_submit_answer import login_and_submit_code
from convert_to_search_format import get_problem_info

def f_process(problem_id):
    load_dotenv()

    username = os.getenv("BAEKJOON_USERNAME")
    password = os.getenv("BAEKJOON_PASSWORD")
    github_token = os.getenv("API_TOKEN")

    query = get_problem_info(problem_id)
    code, submit_lang = main(query, github_token)
    language = submit_lang

    if code:
        success = login_and_submit_code(username, password, str(problem_id), language, code)
        print(f"제출 성공: {success}")
    else:
        print("코드를 가져오는데 실패했습니다.")

# 사용 예시
if __name__ == "__main__":
    problem_id = input("문제 번호를 입력하세요: ")
    f_process(problem_id)