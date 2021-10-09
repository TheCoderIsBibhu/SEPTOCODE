n=int(input())
points=[]
for i in range(n):
    points.append(int(input()))
    # a=points[i]
    if(points[i]>33):
        if(points[i]%10 in {3,4}):
            points[i]=points[i]+5-points[i]%10
        elif(points[i]%10 in {8,9}):
            points[i]=points[i]+10-points[i]%10
for i in range(n):
    print(points[i])
