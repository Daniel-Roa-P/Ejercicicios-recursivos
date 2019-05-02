def binario_a_decimal(n):
    if(n<2):
        return n
    else:
        return n%10 + binario_a_decimal(n/10)*2

print binario_a_decimal(1010)
