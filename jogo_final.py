# Colocamos as funções usadas no jogo no começo do código porque estava dando erro no import. 
# O vs não estava reconhecendo os outros arquivos. 
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
def possui_movimentos_restantes(baralho):
    lista_possivel = []
    for carta in baralho: 
        movimentos = lista_movimentos_possiveis(baralho,baralho.index(carta))
        if movimentos != []: 
            lista_possivel.append('possivel')
    if len(lista_possivel) > 0: 
        return True
    else: 
        return False
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
GREEN = "\033[0;32m"
YELLOW = "\u001b[33m"
MAGENTA = "\u001b[35m"
RESET = "\033[0;0m"
print('Paciência Acordeão')
print('------------------')
print(' ')
print('Seja bem vindo(a) ao jogo Paciência Acordeão! O objetivo do jogo é colocar todas as cartas na mesma pilha!')
print(' ')
print('Regras:')
print(' ')
print('Existem apenas dois movimentos possíveis:')
print('1) Empilhar uma carta sobre a carta imediatamente anterior;')
print('2) Empilhar uma carta sobre a terceira carta anterior.')
print(' ')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:')
print('1) As duas cartas possuem o mesmo valor')
print('                 OU')
print('2) As duas cartas possuem o mesmo naipe.')
print(' ')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')
print(' ')
print(input('Aperte ENTER para começar o jogo: '))
print(' ')
while True:
    print('O estado do baralho atual é: ')
    baralho = cria_baralho()
    i = 1
    for carta in baralho:
        if extrai_naipe(carta) == '♦':
            print( YELLOW + ('{}.{}'.format(i,carta)) + RESET)
        if extrai_naipe(carta) == '♠':
            print( BLUE + ('{}.{}'.format(i,carta)) + RESET)
        if extrai_naipe(carta) == '♥':
            print( RED + ('{}.{}'.format(i,carta)) + RESET)
        if extrai_naipe(carta) == '♣':
            print( GREEN + ('{}.{}'.format(i,carta)) + RESET)
        i += 1
    while possui_movimentos_restantes(baralho):
        escolha_jogador = int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho))))
        if escolha_jogador < 1 or escolha_jogador > len(baralho):
            print('Posição inválida!')
            continue
        movimentos = lista_movimentos_possiveis(baralho, escolha_jogador - 1)
        if movimentos == []:
            print('A carta {} não pode ser movida, escolha outra!'.format(baralho[escolha_jogador - 1]))
            continue
        elif movimentos == [1, 3]:
            repete = True
            while repete:
                print('Sobre qual carta você quer empilhar o {}?'.format(baralho[escolha_jogador - 1]))
                print(MAGENTA + ('1. {}'.format(baralho[escolha_jogador - 2]) + RESET))
                print(MAGENTA + ('2. {}'.format(baralho[escolha_jogador - 4]) + RESET))
                decisao = input('Digite o número de sua escolha (1 ou 2): ')
                if decisao == '1':
                    baralho = empilha(baralho, escolha_jogador - 1, escolha_jogador - 2)
                    c = 1
                    for carta in baralho:
                        if extrai_naipe(carta) == '♦':
                            print( YELLOW + ('{}.{}'.format(c,carta)) + RESET)
                        if extrai_naipe(carta) == '♠':
                            print( BLUE + ('{}.{}'.format(c,carta)) + RESET)
                        if extrai_naipe(carta) == '♥':
                            print( RED + ('{}.{}'.format(c,carta)) + RESET)
                        if extrai_naipe(carta) == '♣':
                            print( GREEN + ('{}.{}'.format(c,carta)) + RESET)
                        c += 1
                    break
                elif decisao == '2':
                    baralho = empilha(baralho, escolha_jogador - 1, escolha_jogador - 4)
                    c = 1
                    for carta in baralho:
                        if extrai_naipe(carta) == '♦':
                            print( YELLOW + ('{}.{}'.format(c,carta)) + RESET)
                        if extrai_naipe(carta) == '♠':
                            print( BLUE + ('{}.{}'.format(c,carta)) + RESET)
                        if extrai_naipe(carta) == '♥':
                            print( RED + ('{}.{}'.format(c,carta)) + RESET)
                        if extrai_naipe(carta) == '♣':
                            print( GREEN + ('{}.{}'.format(c,carta)) + RESET)
                        c += 1
                    break
                else:
                    print('Opção inválida!')
                    continue
            continue
        else:
            if movimentos == [1]:
                baralho = empilha(baralho, escolha_jogador - 1, escolha_jogador - 2)
                c = 1
                for carta in baralho:
                    if extrai_naipe(carta) == '♦':
                        print( YELLOW + ('{}.{}'.format(c,carta)) + RESET)
                    if extrai_naipe(carta) == '♠':
                        print( BLUE + ('{}.{}'.format(c,carta)) + RESET)
                    if extrai_naipe(carta) == '♥':
                        print( RED + ('{}.{}'.format(c,carta)) + RESET)
                    if extrai_naipe(carta) == '♣':
                        print( GREEN + ('{}.{}'.format(c,carta)) + RESET)
                    c += 1
                continue
            else: 
                baralho = empilha(baralho, escolha_jogador - 1, escolha_jogador - 4)
                c = 1
                for carta in baralho:
                    if extrai_naipe(carta) == '♦':
                        print( YELLOW + ('{}.{}'.format(c,carta)) + RESET)
                    if extrai_naipe(carta) == '♠':
                        print( BLUE + ('{}.{}'.format(c,carta)) + RESET)
                    if extrai_naipe(carta) == '♥':
                        print( RED + ('{}.{}'.format(c,carta)) + RESET)
                    if extrai_naipe(carta) == '♣':
                        print( GREEN + ('{}.{}'.format(c,carta)) + RESET)
                    c += 1
                continue
    if len(baralho) == 1:
        print('Parabéns, você ganhou!!!')
    else:
        print('Você perdeu! :( ')
    outro_jogo = input('Você quer jogar novamente? (sim ou nao) ')
    if outro_jogo == 'sim':
        continue
    else:
        break