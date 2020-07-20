import time
import option_rock
import option_run
import intro
import main
def intro():
    print("After a lit night out with friends, you wake up the "
  "next morning in a thick, dark forest. Your head spinning and you're " 
  "fighting the urge to vomit. You stand ther dumbstruck as you marvel at your new, "
  "unfamiliar setting with in utter confusion. The momentary confusion quickly fades when you hear a "
  "eerie sound emitting behind you. Out of nowhere, an ugly slobbering ogre emerges from the bushes and starts "
  "running towards you. Will you..")
    time.sleep(2)
    print("""A. Grab a nearby rock and throw it at the ogre.
    B. Lie down and pretend to be dead hoping it goes away or
    C. Run""")
    choice = input(">>> ").upper().strip()
    if choice in main.answer_A:
        option_rock.option_rock()
    elif choice in main.answer_B:
        print("\nFool! Ogres eat humans. "
        "\n\nYou're dead in a heartbeat. "
        "GAME OVER!!")
    elif choice in main.answer_C:
        option_run.option_run()
    else:
        print(required)
        intro.intro()

intro()