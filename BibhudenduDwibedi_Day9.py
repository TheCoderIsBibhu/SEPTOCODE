t=int(input())
for i in range(t):
    String=input()
    i=0
    count=0
    while(i<len(String)-1):
        if(String[i]=='R' and String[i+1]=='R' or String[i]=='G' and String[i+1]=='G' or String[i]=='B' and String[i+1]=='B'):
            count=count+1
        i=i+1
    print(count)
