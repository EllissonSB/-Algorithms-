a=int(input())
soma=0
lista=[]
if (a==0):
    print("Lista vazia - O valor de S eh zero")
elif(a<0):
    print("O valor informado para N foi negativo")
else:
    for i in range(a):
        e=int(input())
        lista.append(e)
    for j in range(1,(a//2)+1):
        soma+=(lista[j-1]-lista[-j])**2
    if (a%2!=0):
        soma+=(lista[(a//2)])**2
    print("S =",soma)