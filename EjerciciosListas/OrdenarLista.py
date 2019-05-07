def listaOrdenada(Lista):
    if len(Lista) <= 1:
        return True
    elif Lista[0] < Lista[1] and listaOrdenada(Lista[1::]):
        return True
    else:
        return False

Lista = [1,4,3,2,5]

print(listaOrdenada(Lista))