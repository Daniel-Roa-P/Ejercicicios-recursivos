def decimal_a_binario(n):

    if(n<2):
        return n
    else:
        return n%2 + decimal_a_binario(n/2)*10

print decimal_a_binario(8)
