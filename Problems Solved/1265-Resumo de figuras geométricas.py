def quadrado(num):
    if num>0:
        resultado=num**2
    elif num<0:
        resultado=-1
    return resultado
def retangulo(num,num2):
    if num>0 and num2>0:
        resultado=num*num2
    if num<0 or num2<0:
        resultado=-1
    return resultado
def circullo(raio):
    if raio>0:
        resultado=3.14*(raio**2)
    elif raio<0:
        resultado=-1
    return resultado
def final(maior_c,maior_r,maior_q,quantidade,quanditdade_c):
    print("Maior circulo: %.2f"%maior_c)
    print("Maior retangulo: %.2f"%maior_r)
    print("Maior quadrado: %.2f"%maior_q)
    print("Quantidade de figuras",quantidade)
    porc=(quantidade_c/quantidade)*100
    print("Percentual de circulos: %.2f"%porc)
maior_c=0
maior_r=0
maior_q=0
quantidade=0
quantidade_c=0
while True:
    figura=input().upper()
    if figura=="C":
        quantidade_c+=1
        raio=float(input())
        if maior_c==0:
            maior_c=circullo(raio)
        elif maior_c<circullo(raio):
            maior_c=circullo(raio)
    elif figura=="R":
        num=float(input())
        num2=float(input())
        if maior_r==0:
            maior_r=retangulo(num,num2)
        elif maior_r<retangulo(num,num2):
            maior_r=retangulo(num,num2)
    elif figura=="Q":
        l=float(input())
        if maior_q==0:
            maior_q=quadrado(l)
        elif maior_q<quadrado(l):
            maior_q=quadrado(l)

    elif figura=="SAIR":
        break
    quantidade += 1
final(maior_c,maior_r,maior_q,quantidade,quantidade_c)