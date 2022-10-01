import random

class Display:
    """this class will help me print the numbers"""

    def  __init__(num) :
        """my parameter is num and i will generate 2 instances """
        num.value1 = 0
        num.value2 = 0
        num.points = 300
        
        

    def display(num):
        """here i will generate the random number and display the points"""

        num.value1 = random.randint(1,13)
        num.value2 = random.randint(1,13)
        
    



        