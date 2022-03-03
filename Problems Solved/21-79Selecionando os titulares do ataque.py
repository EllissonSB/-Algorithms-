def jogadores(treino,gols,cansado,entrosamento):
    
    indice=treino*2+gols*3.5+cansado*1.5 +entrosamento*2
    if ((treino==0 and gols==0) or ((treino==0 and cansado==0) or((treino==0 and entrosamento==0) or ((cansado==0 and gols==0) or ((cansado==0 and entrosamento==0) or (entrosamento==0 and gols==0)))))):
        indice=0
    return indice
l=[]
for i in range(5):
    nome=input()
    treino=float(input())
    gols=float(input())
    cansado=float(input())
    entrosamento=float(input())
    d=jogadores(treino,gols,cansado,entrosamento)
    l.append(d)
l.sort()
for i in range(1,4):
    print(l[-i])
