import requests

# 백준에서 문제 정답 코드들을 보려면, 깃헙에서 일단 정답을 찾아서 백준에 하나 제출해야함
# 그래서 깃헙에서 정답을 가져오기 위해서 백준에 겁색할 형식으로 return

def get_problem_info(problem_id):
    url = f"https://solved.ac/api/v3/problem/show?problemId={problem_id}"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx

        data = response.json()

        # 난이도를 티어 문자열로 변환
        tier_names = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby", "Unrated"]
        tier = data['level']

        if tier > 0:
            tier_name = tier_names[(tier - 1) // 5]  # 티어 이름 (예: Gold)

            # 티어 레벨을 로마 숫자로 변환
            roman_numerals = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V"}
            tier_level = roman_numerals[5 - ((tier - 1) % 5)]  # 로마 숫자 변환

            result = f"[{tier_name} {tier_level}] Title: {data['titleKo']}"
        else:
            result = f"[Unrated] Title: {data['titleKo']}"

        return result

    except requests.RequestException as e:
        print(f"API 요청 중 오류 발생: {e}")
        return None


# 사용 예시
if __name__ == "__main__":
    problem_id = input("문제 번호를 입력하세요: ")
    result = get_problem_info(problem_id)
    if result:
        print(result)
    else:
        print("문제 정보를 가져오는데 실패했습니다.")