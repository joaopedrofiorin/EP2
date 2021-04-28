def extrai_valor(string):
    return string[:len(string)-1]

def extrai_naipe(string):
    return string[len(string)-1]

def lista_movimentos_possiveis(baralho, indice):
    
    valor = extrai_valor(baralho[indice])
    naipe = extrai_naipe(baralho[indice])
    valor_anterior = extrai_valor(baralho[indice-1])
    naipe_anterior = extrai_naipe(baralho[indice-1])

   
    if indice == 0:
        return []
    if indice == 1 or indice == 2:
        if valor == valor_anterior:
            return [1]
        elif naipe == naipe_anterior:
            return[1]
        else:
            return[]
    else:
        valor_3atras = extrai_valor(baralho[indice-3])
        naipe_3atras = extrai_naipe(baralho[indice-3])
        
        if (valor == valor_anterior or naipe == naipe_anterior) and (valor == valor_3atras or naipe == naipe_3atras):
            return [1, 3]
        elif valor == valor_anterior or naipe == naipe_anterior:
            return [1]
        elif valor == valor_3atras or naipe == naipe_3atras:
            return[3]
        else:
            return[]


