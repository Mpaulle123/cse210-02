
from game.dealer import Dealer

class Director:
    """here i will try to define the code to link both classes"""

    def __init__(self):
        
        self.guess = None
        self.play_again = "y"
        self.score = 300
        self.current_card = 0
        self.next_card = 0
        self.validation = False
        

    def start_game(self):
        """it start and display the text for the beginning of the game"""
        
        while self.play_again == "y":
            dealer = Dealer()
            self.current_card = dealer.random_card()
            print("\nWelcom to Hilo Game.")
            print("You must guess if the next card number is Higher or Lower than the first card.")
            print("*******Let's start*********")
            print(f"\nThe first card is: {self.current_card}")

            self.validation = False

            while self.validation == False:
                self.next_card = dealer.random_card()
                self.guess = input("Higher or Lower? (h/l) ")
                self.evaluate_guess()

            print(f"The Next card was: {self.next_card}")
            print(f"Your score is: {self.score}")

            if (self.score > 0):
                self.play_again = input("Play again? (y/n) ").lower()
            else:
                print("\n********Game Over!********")
                break

    def evaluate_guess(self):
        if (self.guess == "h" or self.guess == "l"):
            self.compute_score()
            self.validation = True
            return self.validation
        else:
            print("Wrong answer... Try again.")
            self.validation = False
            return self.validation

    def compute_score(self):
        

        if self.guess == "h" and self.next_card > self.current_card:
            self.score = self.score + 100

        elif self.guess == "l" and self.next_card > self.current_card:
            self.score = self.score - 75

        elif self.guess == "h" and self.next_card < self.current_card:
            self.score = self.score - 75

        elif self.guess == "l" and self.next_card < self.current_card:
            self.score = self.score + 100

        return self.score
        

        