import time
import intro 
from option_cave import option_cave
from option_rock import option_rock
from option_run import option_run
from option_town import option_town

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

sword = 0
flower = 0

required = ("\nUse only A, B, or C\n")

intro()
option_cave()
option_rock()
option_run()
option_town()

'''playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    intro
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")'''
