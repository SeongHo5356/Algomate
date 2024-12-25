import sys
n = int(sys.stdin.readline())
dic = {0 : [10,10,10,10],  
     1 : [1,1,1,1],
     2 : [2,4,8,6],
     3 : [3,9,7,1],
     4 : [4,6,4,6],
     5 : [5,5,5,5],
     6 : [6,6,6,6],
     7 : [7,9,3,1],
     8 : [8,4,2,6],
     9 : [9,1,9,1]}
for _ in range(n) :
  a, b = map(int, sys.stdin.readline().split())
  print(dic[a%10][b%4-1])