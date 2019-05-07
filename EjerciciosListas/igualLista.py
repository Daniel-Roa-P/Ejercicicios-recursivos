def igualLista(ListaUno, ListaDos):
    if len(ListaUno) != len(ListaDos) or not (ListaUno and ListaDos):
        return False
    elif ListaUno[0] == ListaDos[0] and igualLista(ListaUno[1::], ListaDos[1::]):
        return True
    else:
        return False

ListaUno = [1, 2, 7, 9, 5]
ListaDos = [1, 2, 7, 9, 5]

print(igualLista(ListaUno, ListaDos))