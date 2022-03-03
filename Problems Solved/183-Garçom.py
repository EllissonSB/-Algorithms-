entregas=int(input())
l=[]
anterior=0
acumulador=0
for a in range(entregas):
    entrega=input().split()
    for b in entrega:
        l.append(b)
    for c in l:
        if anterior==0:
            anterior=int(c)
        c=int(c)
        if anterior>c:
            acumulador+=c

    anterior=0
    l=[]
print(acumulador)

