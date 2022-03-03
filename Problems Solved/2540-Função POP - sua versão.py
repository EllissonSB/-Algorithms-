d=int(input())
l=[]
l2=[]
acumulador=0
s1="[ "
s2="[ "

for a in range (d):
    num=int(input())
    l.append(num)
posicao=int(input())
if d==0:
    print("[ ]")
    print("A lista estah vazia - nao eh possivel remover elementos")
elif posicao>d:

    for c in l:
        c=str(c)
        s1+=c+" "
    s1 += "]"
    print(s1)
    print("Nao eh possivel remover o elemento")
else:
    for b in l:
        if acumulador==posicao:
            num=b
        if acumulador!=posicao:
            l2.append(b)
        acumulador+=1

    for c in l:
        c=str(c)
        s1+=c+" "
    for d in l2:
        d=str(d)
        s2+=d+" "
    s1+="]"
    s2+="]"
    print(s1)

    print("O item",num,"serah removido da lista")
    print(s2)
