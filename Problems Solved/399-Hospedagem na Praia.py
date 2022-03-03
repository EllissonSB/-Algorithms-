def praia (x,y):
    if x=="INDIVIDUAL":
        if y>=3:
            total=(125*y)*0.85
        else:
            total=125*y
    elif x=="SU�TE DUPLA":
        if y>=3:
            total=(140*y)*0.85
        else:
            total=140*y
    elif x=="SU�TE TRIPLA":
        if y>=3:
            total=(180*y)*0.85
        else:
            total=180*y
    return (total)
x=input().upper()
y=float(input())
print("%.2f"%praia(x,y))