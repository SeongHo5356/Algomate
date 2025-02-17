str_list = []
return_list =[]
num = int(input()) #hum = 반복횟수

for x in range(num):
    str_list.append(str(input()))

tf = True #참 거짓 판별

for x in range(len(str_list[0])):
    for y in range(num - 1):
        if str_list[y][x] != str_list[y+1][x]:
            tf = False
    if tf == True:
        return_list.append(str_list[0][x])
    else:
        return_list.append('?')
    tf = True

answer = ''.join(return_list)
print(answer)