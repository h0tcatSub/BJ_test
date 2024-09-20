

class Player():
    hands = []
    card_scores = []
    hand_scores = []
    is_win  = False
    is_bust = False
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
        self.calc_hand_score()
        
        if self.hand_scores[0] > 21:
            print("プレイヤー : バースト")
            self.is_bust = True

    
    def calc_hand_score(self):
        for i in range(len(self.hands)):
            self.hand_scores.append(sum(self.card_scores[i]))
