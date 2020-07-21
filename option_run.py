import time
import option_town
import conf

def option_run():
    print ("\nYou run as quickly as possible, but the ogre's "
    "speed is too great to match. You will:")
    
    print ("""A. Hide behind boulder
    B. Get trapped, so you fight
    C. Run towards an abandoned town""")

    time.sleep(2)

    choice = input(">>> ").upper().strip()
    if choice in conf.answer_A:
        print ("You're easily spotted. "
        "\n\nYou're dead!"
        "GAME OVER!!")
    elif choice in conf.answer_B:
        print ("\nYou're no match for an ogre. "
        "\n\nYou dead!"
        "GAME OVER!!!")
    elif choice in conf.answer_C:
        option_town.option_town()
    else:
        print (conf.required)
        option_run()