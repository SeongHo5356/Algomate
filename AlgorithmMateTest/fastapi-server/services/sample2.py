import requests
from bs4 import BeautifulSoup
## 2번

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


if __name__ == "__main__":
    problem_id = input("문제 번호를 입력하세요: ")
    print(check_problem_solved(problem_id)) #True, False