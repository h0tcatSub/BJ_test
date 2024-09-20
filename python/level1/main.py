from Deck import Deck
from Player import Player
from Dealer import Dealer

def start_blackjack():
    deck   = Deck(1)
    player = Player()
    dealer = Dealer()

    while True:
        input("ブラックジャックへようこそ!")


if __name__ == "__main__":
    start_blackjack()