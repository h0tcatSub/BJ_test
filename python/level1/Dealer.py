import Player

class Dealer(Player):

    def hit(self, deck):
        while self.hand_scores[0] < 17:
            super().hit(deck)
            super().calc_hand_score()
            
            if self.hand_scores[0] > 21:
                print("ディーラー : バースト")
                self.is_bust = True