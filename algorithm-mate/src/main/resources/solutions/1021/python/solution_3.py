a=list(range(1,int(input().split()[0])+1))
b=list(map(int,input().split()))
c=0
for i in b:
    x=a.index(i)
    c+=min(x,len(a)-x)
    if x<len(a)-x:
        a=a[x+1:]+a[:x]
    else:
        a=a[x+1:]+a[:x]
print(c)