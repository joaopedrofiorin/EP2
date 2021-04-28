from lista_movimentos_possiveis import lista_movimentos_possiveis
from extrai_naipe import extrai_naipe
from extrai_valor import extrai_valor


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

