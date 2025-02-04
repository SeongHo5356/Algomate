def f(i,p,q):
 if i==m:return 0
 x=q.index(a[i])
 y=min((x-p)%len(q),(p-x)%len(q))
 q.pop(x)
 return y+f(i+1,x,q)
n,m,*a=map(int,open(0).read().split())
q=[*range(1,n+1)]
print(f(0,0,q))