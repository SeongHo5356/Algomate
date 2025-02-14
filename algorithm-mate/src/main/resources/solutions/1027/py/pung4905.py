a=int(input())
output=0
l=list(map(int, input().split()))

for i in range(a):
    index=i
    preindex=index
    prgi=-1000000000
    gi=0
    c=0
    #왼쪽#
    while preindex!=0:
        preindex-=1
        gi=(l[preindex]-l[index])/(index-preindex)
        if gi>prgi:
            c=c+1
            prgi=gi

    #오른쪽#
    preindex=index
    prgi=-1000000000
    while preindex!=a-1:
        preindex+=1
        gi=(l[preindex]-l[index])/(preindex-index)
        if gi>prgi:
            c=c+1
            prgi=gi
    if c>output:
        output=c
print(output)