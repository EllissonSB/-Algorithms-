while (True):
    a=int(input())
    if (a==0):
        break
    elif (a%2!=0):
        p=0
        while (True):
            if((p**2)-((p-1)**2)==a):
                break
            else:
                p+=1
        print(p**2,"-",(p-1)**2)
    else:
        print("a")