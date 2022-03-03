ac_mi=0
ac_ma=0
ac=0
ac2=0
def jogo(x,y):
    igual=0
    a=1
    b=2
    if x=="papel" and y=="pedra":
        return (a)
    elif x=="pedra" and y=="papel":
        return (b)
    elif x=="pedra" and y=="tesoura":
        return (a)
    elif x=="tesoura" and y=="pedra":
        return (b)
    elif x=="tesoura" and y=="papel":
        return (a)
    elif x=="papel" and y=="tesoura":
        return (b)
    if x==y:
        igual+=3
        return(igual)

for i in range(5):
    x=input()
    y=input()
    while True:
        if jogo(x,y)==3:
            x=input()
            y=input()
        else:break
    if jogo(x, y) != 3:
        if jogo(x, y) == 1:
            ac_mi += 1
            ac+=1
        elif jogo(x, y) == 2:
            ac_ma += 1
            ac2+=1

if ac2==5:
    print("MIGUEL")
elif ac==5:
    print("MARIA")
elif ac_ma<ac_mi:
    print("MARIA")
elif ac_mi<ac_ma:
    print("MIGUEL")