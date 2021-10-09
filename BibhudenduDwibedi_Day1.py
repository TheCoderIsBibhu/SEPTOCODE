n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    b=int(input())
    c=int(input())
    arr.append(a+b*c/a-b)


if __name__=="__main__":
    for i in range(n):
        print(arr[i])        
