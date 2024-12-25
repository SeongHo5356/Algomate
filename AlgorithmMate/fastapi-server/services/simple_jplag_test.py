import os
import subprocess


def save_files_as_utf8(directory):
    """
    주어진 디렉토리의 모든 Python 파일을 UTF-8로 다시 저장하는 함수.

    Args:
        directory (str): Python 파일이 포함된 디렉토리 경로
    """
    for filename in os.listdir(directory):
        if filename.endswith(".py"):  # Python 파일만 처리
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()  # 기존 내용을 읽음

            # UTF-8로 다시 저장
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"File saved as UTF-8: {file_path}")


def run_jplag(jplag_path, solutions_path, results_path, language="python3"):
    """
    JPlag를 실행하는 함수.

    Args:
        jplag_path (str): JPlag .jar 파일 경로
        solutions_path (str): 소스 코드 파일들이 위치한 경로
        results_path (str): 결과를 저장할 경로
        language (str): JPlag에서 사용할 언어 옵션 (기본값: python3)
    """
    try:
        command = [
            "java", "-jar", jplag_path,
            "-l", language, "-m", "10",
            "-r", results_path,
            solutions_path
        ]
        print(f"Running JPlag with command: {' '.join(command)}")
        subprocess.run(command, check=True)
        print("JPlag completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during JPlag execution: {e}")


# 메인 코드
if __name__ == "__main__":
    # 경로 설정
    base_path = "C:/Users/kjeng/Desktop/Study/AlgorithmMate/AlgorithmMate/fastapi-server/services/solutions/1012"
    jplag_jar_path = "C:/Users/kjeng/Desktop/jplag_3_0.jar"
    results_path = os.path.join(base_path, "result")

    # Step 1: UTF-8로 파일 저장
    # save_files_as_utf8(base_path)

    # Step 2: JPlag 실행
    run_jplag(jplag_jar_path, base_path, results_path, language="python3")
