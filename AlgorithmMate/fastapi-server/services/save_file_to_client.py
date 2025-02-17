# import os
# import shutil
# from check_code_similarity import run_jplag
#
# def save_top_similarity_files(results, base_path, to_clients_path, keyword = "kjeng7897"):
#     """
#     유사도 상위 2개의 파일을 toClients 폴더에 저장하는 함수.
#
#     Args:
#         results (list of tuples): 유사도 결과 리스트, [(파일1, 파일2, 유사도)]
#         base_path (str): 원본 파일들이 저장된 경로
#         to_clients_path (str): 결과 파일을 저장할 경로
#     """
#     # 유사도 상위 2개 정렬
#     sorted_results = sorted(results, key=lambda x: x[2], reverse=True)[:5]
#     similarities = []
#     for i, (file1, file2, similarity) in enumerate(sorted_results, start=1):
#
#         # 내거 말고 비교한 다른 사람 코드 비교
#         filename1 = file1
#         if (filename1.split('.')[0] == keyword):
#             file2_path = os.path.join(base_path, file2)
#             sample2_path = os.path.join(to_clients_path, f"sample{i}.py")
#             shutil.copy(file2_path, sample2_path)
#             print(f"Copied {file2} to {sample2_path}")
#             similarities.append(similarity)
#
#         else:
#             file1_path = os.path.join(base_path, file1)
#             sample1_path = os.path.join(to_clients_path, f"sample{i}.py")
#             shutil.copy(file1_path, sample1_path)
#             print(f"Copied {file1} to {sample1_path}")
#             similarities.append(similarity)
#
#     return similarities
#
#

# if __name__ == "__main__":
#     # JPlag 실행 예제
#     jplag_path = "C:/Users/kjeng/Desktop/jplag_3_0.jar"
#     solutions_path = "C:/Users/kjeng/Desktop/Study/AlgorithmMate/AlgorithmMate/fastapi-server/services/solutions/1012"
#     results_path = "C:/Users/kjeng/Desktop/Study/AlgorithmMate/AlgorithmMate/fastapi-server/services/solutions/1012/result2"
#     to_clients_path = "C:/Users/kjeng/Desktop/Study/AlgorithmMate/AlgorithmMate/fastapi-server/services/toClients"
#
#     # JPlag 실행 및 유사도 결과 가져오기
#     similarity_results = run_jplag(jplag_path, solutions_path, results_path, language="python3", keyword="kjeng7897")
#
#     # 상위 2개의 유사도 결과 파일 저장
#     save_top_similarity_files(similarity_results, solutions_path, to_clients_path)