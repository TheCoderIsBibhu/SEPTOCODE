t=int(input())
for c in range(t):
    m=int(input())
    l=[]
    for i in range(m):
        k=input()
        k=k.split(" ")
        k=[int(x) for x in k]
        l.insert(i,k)
    add1=sum(l[0])+sum(l[i])
    add2=0
    for i in range(m):
        add2=add2+l[i][0]+l[i][m-1]
    print(abs(add1-add2))