import random

class Dealer:
    """this class will control the display of the cards"""

    def  __init__(self) :
        """ self is the parameter and self.number_card is the instance"""
        
        self.number_card = 0
        
        
        
    def random_card(self):
        """here i will generate the random number and display it for card 1 and 2"""

        self.number_card = random.randint(1,13)
        return self.number_card
        
    



        