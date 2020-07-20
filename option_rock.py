import time
import option_cave
def option_rock():
    print ("\nThe ogre is momentarily stunned, but regains consciousness. He begins "
    "running towards you again. Will you... ")
    time.sleep(2)
    print ("""A. Run
    B. Throw another rock
    C. Run towards the nearby cave""")
    choice = input(">>> ").upper().strip()
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print ("\nYou decided to throw another rock, thinking the first " 
        "rock thrown did much damage. Too bad for you the rock happens to fly well over the "
        "ogre's head. You missed. \n\nYou dead! "
        "GAME OVER!!")
    elif choice in answer_C:
        option_cave.option_cave()
    else:
        print (required)
        option_rock()