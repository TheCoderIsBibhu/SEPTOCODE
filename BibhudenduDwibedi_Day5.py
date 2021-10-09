arr=[[]*40]*10
brr=[[]*40]*10
t=int(input())
for i in range(t):
    n=int(input())
    temp=[]
    for j in range(n):
        temp.append(int(input()))
    arr.insert(i,temp)
i=0
for j in arr:
    temp=[]
    for k in j:
        if j.count(k)==1:
            temp.append(k)
    brr.insert(i,temp)
    i=i+1
for i in brr:
    for j in i:
        print(j,end=" ")
    print("\n")
