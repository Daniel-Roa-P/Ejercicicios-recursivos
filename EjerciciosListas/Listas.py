def igual_lista(a, b):
    if len(a) != len(b):
        return False
    else:
        return True  if not ( a and b ) else a[0] == b[0] and igual_lista(a[1::], b[1::])


a = [1, 2]
b = [1, 2]
print(igual_lista(a, b))