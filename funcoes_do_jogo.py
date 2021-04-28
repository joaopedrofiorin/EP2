import random

def cria_baralho():
    baralho = ['A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'Q♦', 'J♦', 'K♦', 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'Q♠', 'J♠', 'K♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'Q♥', 'J♥', 'K♥', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'Q♣', 'J♣', 'K♣']
    random.shuffle(baralho)
    return baralho 

def extrai_valor(string):
    return string[:len(string)-1]

def extrai_naipe(string):
    return string[len(string)-1]

def empilha(baralho,origem,destino):
    baralho[destino] = baralho[origem]
    del baralho[origem]
    return baralho

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

def possui_movimentos_possiveis(baralho):
    lista_possivel = []
    for carta in baralho: 
        movimentos = lista_movimentos_possiveis(baralho,baralho.index(carta))
        if movimentos != []: 
            lista_possivel.append('possivel')
    if len(lista_possivel) > 0: 
        return True
    else: 
        return False