t=int(input())
for i in range(t):
    n=int(input())
    while(int(n/10)!=0):
        n=str(n)
        sum=0
        for e in n:
            sum=sum+int(e)**2
        n=sum
    if n==1:
        print("lucky")
    else:
        print("unlucky")