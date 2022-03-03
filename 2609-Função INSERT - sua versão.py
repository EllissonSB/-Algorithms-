def printar(lista):
    a="["
    for i in range(len(lista)):
        a+=' '
        a+=str(lista[i])
    a+=' ]'
    return a
a=int(input())
lista=[]
for i in range(a):
    c=int(input())
    lista.append(c)
posi=int(input())
valor=int(input())
andar=0
print(printar(lista))
lista_2=[None]*(len(lista)+1)
if(posi>len(lista)):
    print("A posicao",posi,"estah fora do intervalo")
else:
    for j in range(len(lista_2)):
        if j==posi:
            lista_2[j]=valor
        else:
            lista_2[j]=lista[andar]
            andar+=1
    print(printar(lista_2))