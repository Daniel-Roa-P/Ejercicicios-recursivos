def mostrarUbicacion(Lista, dato):
    if not Lista:
        return None
    if dato == 0:
        return Lista[0]
    else:
        return mostrarUbicacion(Lista[1::], dato-1)

Lista = [5,4,7,8]
print(mostrarUbicacion(Lista, 2))