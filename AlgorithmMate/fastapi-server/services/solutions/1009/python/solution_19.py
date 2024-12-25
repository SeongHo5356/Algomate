from sys import stdin as s

for _ in range(int(input())):
    a,b = map(int,s.readline().strip().split())
    if a%10 == 0:
        print(10)
    else:
        b %= 4
        print((a**(b+4))%10)