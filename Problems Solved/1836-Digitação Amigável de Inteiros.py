l=[]
s=""
s2=""
acumulador=0
acumulador2=0
while True:
    num=input().upper()

    if num=="FIM":
        break
    for i in num:
        if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
            s+=i
        elif i=="O":
            s+="0"
        elif i=="L":
            s+="1"
        else:
            acumulador+=1
    acumulador2=s.__len__()
    for j in s:
        l.append(j)
    for d in range(acumulador2) :
        b=int(l[0])
        if b==0:
            l.pop(0)
    for x in l:
        x=str(x)
        s2+=x

    if acumulador==0:
        print(s2)
    else:
        print("ERRO")
    acumulador=0
    s = ""
    l=[]
    s2=""