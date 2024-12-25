import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10

    # 1 : 1
    # 2 : 4, 8, 6, 2
    # 3 : 9, 7, 1, 3
    # 4 : 6, 4
    # 5 : 5
    # 6 : 6
    # 7 : 9, 3, 1, 7
    # 8 : 4, 2, 6, 8
    # 9 : 1, 9

    if 0 == a:
        print(10)
    elif 1 == a or 5 == a or 6 == a:
        print(a)
    elif 4 == a or 9 == a:
        # 4 : 6, 4
        # 9 : 1, 9
        b = b % 2
        if 1 == b:
            print(a)
        else:
            print((a * a) % 10)
    else:
        # 2 : 4, 8, 6, 2
        # 3 : 9, 7, 1, 3
        # 7 : 9, 3, 1, 7
        # 8 : 4, 2, 6, 8
        b = b % 4
        if 0 == b:
            print((a ** 4) % 10)
        else:
            print((a ** b) % 10)