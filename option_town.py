import time
def option_town():
    print ("\nWhile frantically running, you notice a rusty old "
    "sword lying in the mud. You quickly reach down and grab it, "
    "but miss. You try to calm down as you hide "
    "behind an old abandoned building, waiting for the ogre to come "
    "charging around the corner. You notice a purple flower "
    "near your foot. Will you pick it up? (Y/N)")
    choice = input(">>> ")
    if choice in yes:
        flower = 1 #adds a flower
    else:
        flower = 0
    print ("You hear its heavy footsteps and ready yourself for "
    "the impending ogre.")
    time.sleep(5)
    if flower > 0:
        print ("\nYou quickly hold out the purple flower, somehow "
        "hoping it will stop the ogre.")
        time.sleep(5)
        print("It does! The orc was looking "
        "for love. "
        "\n\nThis got weird, but you survived! CONGRATS!!")
    else: #If the player didn't grab the flower
        print ("\nMaybe you should have picked up the flower. "
        "\n\nYou're dead! "
        "GAME OVER!")