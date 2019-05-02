def potencia(a,b):
    if(b==0):
        return 1
    elif(a==1):
        return 1
    else:
        return a*potencia(a,b-1)

print(potencia(2,6))
