t=int(input())
check='abcdefghijklmnopqrstuvwxyz'
for i in range(t):
    s=input()
    if len(s)<26:
        print('Fail')
    else:
        for ch in check:
            if ch not in s:
                print('Fail')
                break
        else:
            print('Pass')
                