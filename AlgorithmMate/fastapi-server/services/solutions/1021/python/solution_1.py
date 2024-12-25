def solution(n: int, m: int, positions: list) -> int:
    # 1부터 n까지의 숫자로 이루어진 리스트 생성
    lst = list(range(1, n + 1))
    # 회전 연산의 총 횟수를 저장할 변수 초기화
    operations = 0
    
    for position in positions:
        # 현재 리스트에서 찾고자 하는 위치의 인덱스 계산
        idx = lst.index(position)
        
        if idx < len(lst) - idx:
            # 왼쪽으로 회전하는 것이 더 빠른 경우
            operations += idx
            # 리스트를 왼쪽으로 idx만큼 회전
            lst = lst[idx:] + lst[:idx]
        else:
            # 오른쪽으로 회전하는 것이 더 빠른 경우
            operations += len(lst) - idx
            # 리스트를 오른쪽으로 (len(lst) - idx)만큼 회전
            lst = lst[-(len(lst) - idx):] + lst[:-(len(lst) - idx)]
        
        # 첫 번째 요소 제거
        lst.pop(0)
        
    # 총 회전 연산 횟수 반환
    return operations

if __name__ == '__main__':
    # 테스트 케이스 실행 및 결과 출력
    # print(solution(10, 3, [1, 2, 3]))  # expect 0
    # print(solution(10, 3, [2, 9, 5]))  # expect 8
    # print(solution(32, 6, [27, 16, 30, 11, 5, 23]))  # expect 59
    
    # 백준 제출용 코드
    n, m = map(int, input().split())
    positions = list(map(int, input().split()))
    print(solution(n, m, positions))