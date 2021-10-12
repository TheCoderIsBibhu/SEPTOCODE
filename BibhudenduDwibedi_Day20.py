t=int(input())
for i in range(t):
    n=int(input())
    if(n%2==0):print("2 "*int(n/2))
    else:
        print("2 "*int((n-3)/2) +"3")