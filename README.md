# cse210-02
TEAM MEMBERS:
Sam Boothe
Raquel de Freitas Greco Bueno de Freitas Greco Bueno
Paulle MAHOUANGOU
Rubén Zempoalteca Zempoalteca Torres

Program description:

We will have two classes:

The class "Dealer" will control the card numbers (from 1 to 13) and display the first and next card randomly, so we only need:

  class(Dealer)
-------------------------------
(Attributes)
  number_card: from 1 to 13    
-------------------------------
  (Methods)
  random_card()
  _init_(self)

The method "random_card()" will return a random number between 1 and 13. It will be called by the program to assign a random number for the current card and the next card.

The class "Director" will control the game flow, initialize the points of the player with 300 points, evaluate the responses of the player, and call the method " random_card()" from the class "Dealer" to assign a random number for the current card and the next card and compute the score. The "class" will be:

 class(Director)
---------------------
  (Attributes)
  score # Initializing the score to 300.
  guess #Higher or lower (h/l)
  play_again #Higher or lower(y/n)
  current_card #Value of the first card
  next_card #Value of the second card
  validation #Validate if the player answer "h" or "l" if wrong send an error message    
---------------------
  (Methods)
  start_game()
  evaluate_guess() (h/l)
  compute_score()
  _init_(self)

The method "start_game()":
Starts the game by displaying a card number between 1 to 13.
Asks the user to guess whether the next card will be higher or lower.
It evaluates the user's guess and updates the score.
It asks the user if they want to play again.
If the user's score is greater than 0, the user can play again.
If the user's score is less than or equal to 0, the game is over.

The method "evaluate_guess()":
If the guess is either "h" or "l", then compute the score. Otherwise, print "Wrong answer... Try again."

The method "compute_score()":
If the guess is correct, the score is increased by 100. If the guess is incorrect, the score is decreased by 75. The score is being returned.
