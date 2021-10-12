t=int(input())
for i in range(t):
    count=1
    x=int(input())
    while(x!=1):
        if(x%2==0):x=int(x/2)
        else:
            count+=1
            x=int((x-1)/2)
    print(count)