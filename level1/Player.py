

class Player():
    hands = []
    card_scores = []
    hand_scores = []
    is_blackjack = False

    def hit(self, deck):
        card = deck.deal()
        self.hands.append(card)
        
        if card.score == "T":
            card.score = 10
        elif card.score == "J":
            card.score = 10
        elif card.score == "Q":
            card.score = 10
        elif card.score == "K":
            card.score = 10
        
        self.card_scores.append(card.score)
    
    def stand(self):
        for i in range(len(self.hands)):
            self.hand_scores.append(sum(self.card_scores[i]))
