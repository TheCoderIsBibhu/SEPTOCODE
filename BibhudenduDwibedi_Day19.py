t=int(input())
for i in range(t):
    n=int(input())
    arr=input().split(" ")
    arr=[int(x) for x in arr]
    k=0
    for x in range(n-1):
        if(arr[x]==arr[x+1]):
            k=1
            break
    print("Gentle") if k==1 else print("Steep")

        
