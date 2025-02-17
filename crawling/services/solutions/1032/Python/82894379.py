n = int(input())

str1 = input()

if n != 1:
    for i in range(n-1):
        str2 = input()
        for j in range(len(str2)):
            if str1[j] != str2[j]:
                str1 = str1[:j]+"?"+str1[j+1:]
print(str1)