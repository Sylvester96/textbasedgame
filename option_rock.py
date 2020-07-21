import time
import option_run
import conf
import option_cave

def option_rock():
    print ("\nThe ogre is momentarily stunned, but regains consciousness. He begins "
    "running towards you again. Will you... ")
    
    print ("""A. Run
    B. Throw another rock
    C. Run towards the nearby cave""")
    time.sleep(2)

    choice = input(">>> ").upper().strip()
    if choice in conf.answer_A:
        option_run.option_run()
    elif choice in conf.answer_B:
        print ("\nYou decided to throw another rock, thinking the first " 
        "rock thrown did much damage. Too bad for you the rock happens to fly well over the "
        "ogre's head. You missed. \n\nYou dead! "
        "GAME OVER!!")
    elif choice in conf.answer_C:
        option_cave.option_cave()
    else:
        print (conf.required)
        option_rock()