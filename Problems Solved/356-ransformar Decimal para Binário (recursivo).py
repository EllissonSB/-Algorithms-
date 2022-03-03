a=int(input())
def d(n):
    if n == 0:
        return ""
    else:
        return d(n//2)+str(n%2)
b=d(a)
if a==0:
    print(0)
else:
    for i in b:
        print(i)