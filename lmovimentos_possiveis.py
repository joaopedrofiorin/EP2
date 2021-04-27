def extrai_valor(string):
    return string[:len(string)-1]

def extrai_naipe(string):
    return string[len(string)-1]

def lista_movimentos_possiveis(baralho, indice):
    if indice > len(baralho) - 1:
        return 'Valor inválido'
    if indice == 0:
        return []
    valor = extrai_valor(baralho[indice])
    naipe = extrai_naipe(baralho[indice])
    valor_anterior = extrai_valor(baralho[indice-1])
    naipe_anterior = extrai_naipe(baralho[indice-1])
    if indice == 1 or indice == 2:
        if valor == valor_anterior:
            return [1]
        elif naipe == naipe_anterior:
            return[1]
        else:
            return[]

print(lista_movimentos_possiveis(['J♥', 'J♥', 'Q♣', 'K♠', '10♣'], 1))