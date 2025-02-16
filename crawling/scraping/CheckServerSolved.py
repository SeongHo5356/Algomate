from bs4 import BeautifulSoup
import requests

# 서버계정이 이미 백준에서 해당 문제의 정답에 접근 가능한지 알아보는 파일
# 계정이 정답을 제출한 적 있으면 바로 크롤링 가능
# 계정이 정답을 제출한 적 없으면, 깃헙에서 정답을 찾아서 제출하고 크롤링 가능

def check_problem_solved(problem_number):
    data = get_all_problems("robot3104")
    # # 전체 리스트 solved, attempt but not solved. .. 모든 리스트에서 탐색
    # return any(problem_number in data[key] for key in data)
    return int(problem_number) in data['solved']



def get_all_problems(username):
    url = f"https://www.acmicpc.net/user/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, "html.parser")
    problem_status = {
        "solved": [],
        "partially_solved": [],
        "attempted_but_not_solved": []
    }
    sections = soup.find_all("div", class_="problem-list")
    section_titles = ["맞은 문제", "맞았지만 만점을 받지 못한 문제", "시도했지만 맞지 못한 문제"]

    for index, section in enumerate(sections):
        problems = [int(problem_id.text) for problem_id in section.find_all("a")]
        if section_titles[index] == "맞은 문제":
            problem_status["solved"] = problems
        elif section_titles[index] == "맞았지만 만점을 받지 못한 문제":
            problem_status["partially_solved"] = problems
        elif section_titles[index] == "시도했지만 맞지 못한 문제":
            problem_status["attempted_but_not_solved"] = problems

    return problem_status

# 사용 예시
if __name__ == "__main__":
    print(get_all_problems("robot3104"))
    print(check_problem_solved(1002))