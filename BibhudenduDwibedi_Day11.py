t=int(input())
for i in range(t):
    count=0
    n=int(input())
    while(n!=1):
        n=int(n/2)
        count+=1
    print(count)