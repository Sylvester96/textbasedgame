import time
import intro
import conf

'''intro.intro()
option_cave.option_cave()
option_rock.option_rock()
option_run.option_run()
option_town.option_town()'''

def game():
    playAgain = "yes"
    while playAgain == "yes" or playAgain == "y":
        intro.intro()
        playAgain = input("Do you want to play again? (yes or y to continue playing): ")

if __name__ == "__main__":
    game()
