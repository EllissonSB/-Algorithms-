def tt(letras):
    acu = 0
    s = ""
    acumulador=0
    if letras=="":
        print(0)
    for i in letras:
        if i=="1" or i=="2" or i=="2" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
            print("numeros")
            print(0)
            acu=1
            break
    if acu!=1:
        letras2=letras.replace("A","@")
        letras=""
        letras=letras2.replace("a","@")
        letras2=""
        letras2=letras.replace("e","3")
        letras=""
        letras=letras2.replace("E","3")
        letras=""
        letras=letras2.replace("i","1")
        letras2=""
        letras2=letras.replace("I","1")
        letras=""
        letras=letras2.replace("o","0")
        letras2=""
        letras2=letras.replace("O","0")
        letras=""
        letras=letras2.replace("t","7")
        letras2=""
        letras2=letras.replace("T","7")
        letras=""
        letras=letras2.replace("s","5")
        letras2=""
        letras2=letras.replace("S","5")
        contador=len(letras2)
        for i in range(1,contador+1):
            s+=letras2[-i]
        print(s)
        for i in s:
            if i=="@" or i=="3" or i=="1" or i=="0" or i=="7" or i=="5":
                acumulador+=1
        print(acumulador)
letras=input()
tt(letras)