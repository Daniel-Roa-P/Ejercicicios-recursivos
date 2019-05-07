def contarPares(Lista):
    if not Lista:
        return 0
    elif Lista[0] % 2 == 0:
        return 1 + contarPares(Lista[1::])
    else:
        return contarPares(Lista[1::])

Lista = [2,3,5,6,10]

print(contarPares(Lista))