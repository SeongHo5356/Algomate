T, *temp = map(int, open(0).read().split())
case = [[x,y] for x, y in zip(temp[0::2], temp[1::2])]

for a, b in case:
    answer = 1
    b = (b-1)%4+1
    while b: answer = (answer*a-1)%10+1; b-=1
    print(answer)