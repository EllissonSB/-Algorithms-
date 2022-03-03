def willy(s):
    if len(s)==0:
        return 0
    else:
        if int(s[0])%2==0:
            return int(s[0]) * 2 * len(s) + int(willy(s[1:]))
        else: 
            return int(s[0]) * 3 * len(s) + int(willy(s[1:]))

while True:
    n=input()
    if n=='0':break
    print(willy(n))