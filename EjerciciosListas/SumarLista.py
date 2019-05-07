def sumarLista(Lista):
    if not Lista:
        return 0
    else:
        return Lista[0] + sumarLista(Lista[1::])

Lista = [5,4,7,8]
print(sumarLista(Lista))