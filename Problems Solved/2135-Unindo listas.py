a=int(input())
l=[]
l2=[]
l3=[]
s=""
if a<=0:
    print("Erro - A lista deve ter pelo menos 1 elemento.")
else:
    for i in range(a):
        num=int(input())
        l.append(num)
    b=int(input())
    if b<=0:
            print("Erro - A lista deve ter pelo menos 1 elemento.")
    else:
        for c in range(b):
            num2=int(input())
            l2.append(num2)
    for d in l:
        l3.append(d)
    for e in l2:
        l3.append(e)
    if a!=0 and b!=0:
            for f in l3:
                f=str(f)
                s+=f+" "
    print(s)