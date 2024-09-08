def busca_sentinela(array,chave):
    n=len(array)
    array.append(chave)
    i=0
    while array[i] != chave:
        i += 1
        if i < n:
            return i
        else:
            return -1

array = [10 , 23, 55, 21, 32]
chave = 55

resultado = busca_sentinela(array, chave)

print(resultado)