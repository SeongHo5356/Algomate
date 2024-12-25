import sys
input = sys.stdin.readline
one=['1','5','6']
two=[2,4, 8, 6]
three=[3, 9, 7, 1]
seven=[7,9,3,1]
eight=[8,4,2,6]

t=int(input())
for i in range(t):
    a,b=map(str,input().split())
    if a[-1] =='0':
        print(10)
    elif a[-1] in one:
        print(a[-1])
    elif a[-1]=='2':
        print(two[(int(b)-1)%4])
    elif a[-1]=='3':
        print(three[(int(b)-1)%4])
    elif a[-1]=='4':
        if int(b)%2==1:
            print(4)
        else:
            print(6)
    elif a[-1]=='7':
        print(seven[(int(b)-1)%4])
    elif a[-1]=='8':
        print(eight[(int(b)-1)%4])
    elif a[-1]=='9':
        if int(b)%2==1:
            print(9)
        else:
            print(1)