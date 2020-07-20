import time
def option_run():
    print ("\nYou run as quickly as possible, but the ogre's "
    "speed is too great to match. You will:")
    time.sleep(2)
    print ("""A. Hide behind boulder
    B. Get trapped, so you fight
    C. Run towards an abandoned town""")
    choice = input(">>> ").upper().strip()
    if choice in answer_A:
        print ("You're easily spotted. "
        "\n\nYou're dead!"
        "GAME OVER!!")
    elif choice in answer_B:
        print ("\nYou're no match for an ogre. "
        "\n\nYou dead!"
        "GAME OVER!!!")
    elif choice in answer_C:
        option_town()
    else:
        print (required)
        option_run()