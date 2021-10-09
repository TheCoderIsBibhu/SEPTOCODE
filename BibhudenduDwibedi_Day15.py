t=int(input())
for i in range(t):
    n=int(input())
    students=input()
    students=students.split(" ")
    students=[int(x) for x in students]
    for k in range(1,n+1):
        if k not in students:
            print(k)
            break
    else:
        print(0)