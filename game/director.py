
from game.dealer import Dealer

class Director:
    """
    The class "Director" will control the game flow, initialize the points of the player with 300 points,
    evaluate the responses of the player and compute the score.
    
    """
    def __init__(self):
        
        self.guess = None
        self.play_again = "y"
        self.score = 300
        self.current_card = 0
        self.next_card = 0
        self.validation = False
        

    def start_game(self):
        """
        The function starts the game by displaying a card number between 1 to 13.

        The function then asks the user to guess whether the next card will be higher or lower.

        The function then evaluates the user's guess and updates the score.

        The function then asks the user if they want to play again.

        If the user's score is greater than 0, the user can play again.

        If the user's score is less than or equal to 0, the game is over.
        """

        while self.play_again == "y":
            #the while loop will restart the game at this point 
            # dealer is new instance of Dealer
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
        """
        If the guess is either "h" or "l", then compute the score and set validation to True. Otherwise,
        print "Wrong answer... Try again." and set validation to False.
        :return: The validation variable is being returned.
        """
        
        if (self.guess == "h" or self.guess == "l"):
            self.compute_score()
            self.validation = True
            return self.validation
        else:
            print("Wrong answer... Try again.")
            self.validation = False
            return self.validation

    def compute_score(self):
        """
        If the guess is correct, the score is increased by 100. If the guess is incorrect, the score is
        decreased by 75
        :return: The score is being returned.
        """

        if self.guess == "h" and self.next_card > self.current_card:
            self.score = self.score + 100

        elif self.guess == "l" and self.next_card > self.current_card:
            self.score = self.score - 75

        elif self.guess == "h" and self.next_card < self.current_card:
            self.score = self.score - 75

        elif self.guess == "l" and self.next_card < self.current_card:
            self.score = self.score + 100

        return self.score
        

        