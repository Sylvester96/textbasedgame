import time
def option_cave():
    print("\nYou are hesitant, since the cave was dark, creepy and "
    "ominous. Before you completely enter, you notice a shiny knightly sword lying on "
    "the ground. Do you pick up a sword? (Y/N)")
    choice = input(">>> ").lower().strip()
    if choice in yes:
        sword = 1
    else:
        sword = 0
    print("\nWhat do you do next?")
    time.sleep(2)
    print("""A. Hide in silence
    B. Fight
    C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
        print("\nYou're really going to hide in the dark? I think "
        "ogres can see very well in the dark, so...\n\nYou dead! "
        "GAME OVER!!")
    elif choice in answer_B:
        if sword > 0:
            print("\nYou stay and wait. The shimmering sword attractS "
            "the ogre, which underestimates you and thinks you were no match. As he walks "
            "closer and closer, your heart beats rapidly. As the ogre "
            "reaches out to grab the sword, you catch it offguard and pierce the blade into "
            "its chest instantly killing it on the spot. \n\nYou survived! CONGRATS!!")
        else: #if the sword was not grabbed by the player
            print("\nYou should've picked the sword. You're "
            "defenseless. \n\nYou dead! " 
            "GAME OVER!!")
    elif choice in answer_C:
        print ("As the ogre enters the dark cave, you silently "
        "sneak out. While trying to sneak out, your sword accidentally drops and the ogre hears it. It immediately turns to your direction "
        "and runs after you.")
        option_run()
    else:
        print (required)
        option_cave() 