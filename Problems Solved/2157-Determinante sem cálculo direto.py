m=[]
zero=0
linha_=""
coluna=''
anterior=""
acumulador=0
while True:
    a=input().upper()
    if a=="ACABOU":
        break
    a=a.split()
    m.append(a)
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]=="0":
            zero+=1
    if zero==len(m[i]):
        print("Determinante zero.")
        acumulador += 1
        break

    zero=0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[j][i]=="0":
            zero+=1
    if zero==len(m[i]):
        print("Determinante zero.")
        acumulador += 1
        break

    zero=0
for i in range(len(m)):
    if i==0:
        linha_=m[i]
    elif linha_==m[i]:
        print("Determinante zero.")
        acumulador += 1
        break

for i in range(len(m)):
    for j in range(len(m[i])):
        coluna+=m[j][i]+" "
    if i==0:
        anterior=coluna
    elif anterior==coluna:
        print("Determinante zero.")
        acumulador += 1
        break

    coluna=""
if acumulador==0:
    print("Determinante diferente de zero.")