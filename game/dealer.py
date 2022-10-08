import random


class Dealer:
    """
    The class "Dealer" will control the card numbers (from 1 to 13) and display randomly the first and next card.
    

    Attributes
    number_card (int): set cards from 1 to 13

    """

    def __init__(self):
        """
        Constructs a new instance of Dealer.
        Args:
        self (Dealer): An instance of Dealer.
        """
        self.number_card = 0

    def random_card(self):
        """
        It returns a random number between 1 and 13
        :return: The number of the card.
        """
        self.number_card = random.randint(1, 13)
        return self.number_card
