a=float(input())
b=float(input())
c=input().upper()
if c=="SOMA":
    resultado=a+b
elif c=="SUBTRACAO":
    resultado=a-b
elif c=="DIVISAO":
    resultado=a/b
elif c=="MULTIPLICACAO":
    resultado=a*b
print("resultado = %.2f"%resultado)