import os
from dotenv import load_dotenv

from baekjoon_find_answer import main
from baekjoon_submit_answer import login_and_submit_code
from convert_to_search_format import get_problem_info

# 번호를 파라미터로 받고 해당 정답을 깃헙에서 찾고, 백준에 제출
def f_process(problem_id):
    load_dotenv()

    username = os.getenv("BAEKJOON_USERNAME")
    password = os.getenv("BAEKJOON_PASSWORD")
    github_token = os.getenv("API_TOKEN")

    query = get_problem_info(problem_id) # 깃헙에서 검색할 수 있는 형식으로 변환
    code, submit_lang = main(query, github_token) # 정답 코드, 해당 코드 언어
    language = submit_lang

    if code:
        # 정답을 찾으면 해당 코드를 정답으로 제출
        success = login_and_submit_code(username, password, str(problem_id), language, code)
        print(f"제출 성공: {success}")
    else:
        # 정답을 못 찾음
        print("코드를 가져오는데 실패했습니다.")

# 사용 예시
if __name__ == "__main__":

    # problem_id = "1027"
    #
    # searchFormat = convertToGithubSearchFormat(problem_id)
    # code, submitLang = findAnswerFromGithub(searchFormat)
    #
    # if code:
    #     success = login_and_submit_code(problem_id, submitLang, code)
    #     print(f"제출 성공: {success}")
    # else:
    #     print("코드를 가져오는데 실패했습니다.")

    problem_id = input("문제 번호를 입력하세요: ")
    f_process(problem_id)
