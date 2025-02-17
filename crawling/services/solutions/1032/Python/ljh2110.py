num = int(input())
str1 = list(input())
len = len(str1)

for _ in range(num-1):
    str2 = input()
    for i in range(len):
        if str1[i] != str2[i]:
            str1[i] = "?"

for i in str1:
    print(i, end="")