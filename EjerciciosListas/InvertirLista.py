def invertirLista(Lista):
    if not Lista:
        return Lista
    else:
        return [Lista[-1]] + invertirLista(Lista[0:-1])

Lista = [7,8,2,5]
print(invertirLista(Lista))