t=int(input())
for i in range(t):
    n=int(input())
    arr=input()
    arr=arr.split(" ")
    arr=[int(x) for x in arr]
    max1=max(arr)
    print(arr.index(max1)+1)