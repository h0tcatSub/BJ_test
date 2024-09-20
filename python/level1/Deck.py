import uuid
import random
import hashlib

class Deck:
    suits = {"c", "s", "h", "d"}
    scores = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    cards = []

    def __init__(self, deck_amount):
        self.set_deck(deck_amount)
        self.shuffle()
    
    def set_deck(self, deck_amount):
        for i in range(deck_amount):
            for suit in self.suits:
                for score in self.scores:
                    if score == 1:
                        score = "A"
                    elif score == 10:
                        score = "T"
                    elif score == 11:
                        score = "J"
                    elif score == 12:
                        score = "Q"
                    elif score == 13:
                        score = "K"
                    card = f"{score}{suit}"
                    self.cards.append(card)
     
    def shuffle(self):
        seed = uuid.uuid4()
        random.seed(hashlib.sha256(seed).hexdigest())
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop(0)