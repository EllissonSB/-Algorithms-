nl, nc = input().split()
lm, soma, menor, cont = [], 0, 0, 0

for i in range(int(nl)):
    lm+=[input().split()]
for i in range(int(nc)):
    soma = 0
    for j in range(int(nl)):
        soma+=int(lm[j][i])
    if i==0:menor=soma
    if soma<menor:menor=soma 
print(menor)