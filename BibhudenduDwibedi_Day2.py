def isLeap(x):
    if x%400==0:
        return 366
    else:
        if x%100==0:
            return 365
        elif x%4==0:
            return 366
        else:
            return 365

t=int(input())
result=[]
for i in range(t):
    a,b=input().split()
    a=int(a)
    b=int(b)
    a=isLeap(a)
    b=isLeap(b)
    result.append(a+b)
for i in range(t):
    print(result[i])


