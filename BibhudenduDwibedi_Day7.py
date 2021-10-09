t=int(input())
for i in range(t):
    n=int(input())
    String=input()
    if("000000" in String or "111111" in String):
        print("YES")
    else:
        print("NO")