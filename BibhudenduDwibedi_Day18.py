t=int(input())
for i in range(t):
    n=int(input())
    arr=input().split(" ")
    arr=[int(x) for x in arr]
    for k in range(1,n+1):
        if k not in arr:
            print(k,end=" ")
    print("\n")