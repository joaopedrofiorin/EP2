import random
from termcolor import colored

def cria_baralho(): 
    baralho =[]
    
    baralho.append(colored(['A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'Q♦', 'J♦', 'K♦'], 'red'))
    baralho.append(colored(['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'Q♠', 'J♠', 'K♠'], 'blue'))
    baralho.append(colored(['A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'Q♥', 'J♥', 'K♥'], 'green'))
    baralho.append(colored(['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'Q♣', 'J♣', 'K♣'], 'yellow'))

    random.shuffle(baralho)
    return baralho   


print(cria_baralho())