d=int(input())
l=[]
l2=[]
acumulador=0
s1="[ "
s2="[ "
decisao=-1

for a in range (d):
    num=int(input())
    l.append(num)
posicao=int(input())
if d==0:
    print("[ ]")
    print("A lista estah vazia - nao eh possivel remover elemento")

else:
    for b in l:
        if b!=posicao:
            l2.append(b)
        if b==posicao:
            decisao=0


    if decisao==0:
        for c in l:
            c=str(c)
            s1+=c+" "
        for d in l2:
            d=str(d)
            s2+=d+" "
        s1+="]"
        s2+="]"
        print(s1)
        print(s2)
    else:

        for c in l:
            c=str(c)
            s1+=c+" "
        s1 += "]"
        print(s1)
        print("Nao eh possivel remover o elemento", posicao)