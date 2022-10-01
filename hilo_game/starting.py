
from hilo_game.numb import Display

class general:
    """here i will try to define the code to link both classes"""

    def __init__(num):
        
        num.is_playing = True
        num.score = 300
        num.total_score = 0
        

        

    def start_game(num):

        while num.is_playing:
            num.get_inputs()
    
            num.do_outputs()

    def get_inputs(num):
        display = Display()

        display.value1
        display.value1
        print(f"The card is:" + display.value1)
        guess = input("Higher or Lower (h/l)?")
        print(f"The nextcard was:" + display.value1)

        if guess == "h" and display.value1 >= display.value2:
            display.points += 100

        elif guess == "l" and display.value1 >= display.value2:
            display.points += -75

        elif guess == "h" and display.value1 < display.value2:
            display.points += -75

        elif guess == "l" and display.value1 < display.value2:
            display.points += 100


        play_again = input("Play again? (y/n) ")
        num.is_playing = (play_again == "y" , "Y")

        if not num.is_playing:
            return
        
        

        num.score += display.points
        num.total_score += num.score


    def do_outputs(num):
        
        if not num.is_playing:
            return

        print(f"your score is:{num.total_score}")
        num.is_playing == (num.total_score>0)
