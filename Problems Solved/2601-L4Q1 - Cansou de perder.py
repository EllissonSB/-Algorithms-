lm=[]
jogador=""
local=""
verificador=0
for i in range(3):
    lm+=[input().split()]
aleat=input()
nj=int(input())
for i in range(nj):
    jogador=''
    x,y, z = input().split()
    x=x.upper()
    if (int(y)<0) or (int(y)>2) or (int(z)<0) or int(z)>2:
        print('O Dark Souls afetou sua cabe�a? Jogue dentro das demarca��es do jogo.')
    else:
        if x=='X':
            jogador='Eduardo'
        elif x=='O':
            jogador='Leonardo'
        if lm[int(y)][int(z)]!='*':
            print('%s n�o trapacei ou ent�o vamos voltar a jogar Dark Souls.'%jogador)
        else:
            lm[int(y)][int(z)]=x
            print('%s efetuou sua jogada com sucesso.'%jogador)
        if verificador==0:
            for j in range(len(lm)):
                if (lm[j][0]==lm[j][1]==lm[j][2]) and lm[j][0]!='*':
                    ganhador, local, verificador = jogador, 'linha %i.'%(j+1), 1
                    break
                elif (lm[0][j]==lm[1][j]==lm[2][j]) and lm[0][j]!='*':
                    ganhador, local, verificador = jogador, 'coluna %i.'%(j+1), 1
                    break
            if (lm[0][0]==lm[1][1]==lm[2][2]) and lm[0][0]!='*':ganhador, local, verificador = jogador, 'diagonal principal.', 1
            elif(lm[0][2]==lm[1][1]==lm[2][0]) and lm[0][2]!='*':ganhador, local, verificador = jogador, 'diagonal secundaria.', 1

if verificador==0:
    print('Nem no jogo da velha conseguimos ganhar algo, vamos voltar para o Dark Souls.')
else:
    print('%s ganhou o jogo na %s'%(ganhador, local))
for i in range(len(lm)):
    for j in range(len(lm[i])):
        if j!=len(lm[i])-1:print(lm[i][j], end=' ')
        else:print(lm[i][j])