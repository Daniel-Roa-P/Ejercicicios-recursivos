def mayorLista(Lista):
    if not Lista:
        return 0
    elif len(Lista) <= 1:
        return Lista[0]
    else:
        return Lista[0] if Lista[0] > mayorLista(Lista[1::]) else mayorLista(Lista[1::])

Lista = [1, 4, 7, 2, 5]

print(mayorLista(Lista))