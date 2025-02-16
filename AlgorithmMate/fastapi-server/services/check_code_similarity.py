import subprocess

def run_jplag(jplag_path, solutions_path, results_path, language="python3", keyword="kjeng7897"):
    """
    JPlag을 실행하고 특정 키워드가 포함된 결과를 필터링합니다.

    Args:
        jplag_path (str): JPlag .jar 파일 경로.
        solutions_path (str): 분석 대상 소스코드가 위치한 경로.
        results_path (str): 결과를 저장할 경로.
        language (str): JPlag에서 사용할 언어 옵션 (기본값: python3).
        keyword (str): 결과에서 필터링할 키워드 (기본값: "kjeng7897").

    Returns:
        list: 유사도 결과 리스트 [(파일1, 파일2, 유사도)].
    """
    command = [
        "java","-verbose", "-jar", jplag_path,
        "-l", language,
        "-r", results_path,
        solutions_path
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
        print("JPlag 실행 결과 (필터링된 출력):\n")
        print(command)

        similarity_results = []
        # 결과를 줄 단위로 처리
        for line in result.stdout.splitlines():
            # 유사도 결과 추출 (예: Comparing file1-file2: 50.0)
            if "Comparing" in line and ":" in line:
                parts = line.split(":")
                similarity = float(parts[1].strip())  # 유사도 점수
                files = parts[0].replace("Comparing", "").strip().split("-")
                file1, file2 = files[0].strip(), files[1].strip()

                # 키워드가 파일 이름 중 하나에 포함되어 있는지 확인
                if keyword in file1 or keyword in file2:
                    similarity_results.append((file1, file2, similarity))
                    print(line)  # 필터링된 결과 출력

            # "Writing matches"와 "Report exported" 포함된 줄 출력
            elif "Writing matches" in line or "Report exported" in line:
                print(line)

        return similarity_results  # 필터링된 유사도 결과 반환

    except subprocess.CalledProcessError as e:
        print("JPlag 실행 중 오류 발생:", e.stderr)
        print(e)
        return []

if __name__ == "__main__":
    # JPlag 실행 예제

    base_directory = "services/solutions"
    problem_number = "16144"
    #solutions_path = base_directory + "/" + str(problem_number)
    #results_path = base_directory + "/" + str(problem_number) + "/result2"

    jplag_path = "C:/Users/kjeng/Desktop/jplag_5_1.jar"
    solutions_path = "C:/Users/kjeng/Desktop/Study/Algomate/Algomate/AlgorithmMate/fastapi-server/services/solutions/1012/python"
    # solutions_path = "C:/Users/kjeng/Desktop/test/BS-18870"
    results_path = "C:/Users/kjeng/Desktop/Study/Algomate/Algomate/AlgorithmMate/fastapi-server/services/solutions/1012/python/result2"
    # results_path = "C:/Users/kjeng/Desktop/test/result_2"

    run_jplag(jplag_path, solutions_path, results_path, language="python3", keyword="kjeng7897")