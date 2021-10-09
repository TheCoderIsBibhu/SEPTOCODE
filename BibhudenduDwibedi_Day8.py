t=int(input())
for i in range(t):
    String=input()
    j,k=0,0
    for char in String:
        if char.isupper():
            j=j+1
        if char.islower():
            k=k+1
    if j>k:
        print(String.upper())
    else:
        print(String.lower())