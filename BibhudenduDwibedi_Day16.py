t=int(input())
for i in range(t):
    n=int(input())
    arr=input().split(" ")
    arr=[int(x) for x in arr]
    b=[] 
    c=[]
    for ele in arr:
        if(ele%2==0): b.append(ele)
        else: c.append(ele)
    if(len(b)==1): print(arr.index(b[0])+1)
    else: print(arr.index(c[0])+1)

