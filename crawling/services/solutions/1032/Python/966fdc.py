N = int(input())
patt = []

for i in range(N):
    patt.append(input())

length = len(patt[0])

for i in range(length):
    check = patt[0][i]
    isIt = True
    
    for j in range(1, N):
        if patt[j][i] != check:
            isIt = False
            breakpoint

    if isIt:
        print(patt[0][i], end="")
    else:
        print("?", end="")