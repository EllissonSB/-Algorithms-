n=int(input())
l=[]
for i in range(n):
    n2=int(input())
    l.append(n2)
n3=int(input())
l2=l[(n3):n+1]+l[0:n3]
for e in l2: print(e)