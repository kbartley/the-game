import random
import sys
from classes.game import Game

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Error! You need to start game with two integer arguments first number of computers and then number of humans.\nExample: \"python3 ./ 3 0\"")    
    thegame = Game()
    deck = list(range(2,99))
    random.shuffle(deck)
    print(deck)

