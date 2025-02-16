n = int(input())
arr = list(map(int, input().split(' ')))

def get_m(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def r_b_building(arr, n1):
    is_first = True
    cnt = 0
    for i in range(n1, len(arr)-1):
        if is_first or m < get_m(n1, arr[n1], i+1, arr[i+1]):
            is_first = False
            m = get_m(n1, arr[n1], i+1, arr[i+1])
            cnt = cnt + 1
 
    return cnt

def l_b_building(arr, n2):
    is_first = True
    cnt = 0
    for i in range(1, n2+1):
        if is_first or m > get_m(n2, arr[n2], n2-i, arr[n2-i]): 
            m = get_m(n2, arr[n2], n2-i, arr[n2-i])
            is_first = False
            cnt = cnt + 1
            
    return cnt

sum_v = 0
ans = 0
for i in range(0, n):
    sum_v = 0
    if i != n-1: # right
        sum_v = sum_v + r_b_building(arr, i)

    if i != 0: # left
        sum_v = sum_v + l_b_building(arr, i)
    
    if sum_v > ans:
        ans = sum_v

print(ans)