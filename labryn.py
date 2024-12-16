def entrance():
    print("You have entered the dungeon.")
    print("What do you want to do?")
    answer = input("1) Go to the living room \n2) Stay here \n")

    if answer == "1":
        print("You approach the door ahead and open it.")
        livingroom()
    elif answer == "2":
        print("You have decided to stay for a while.")
        entrance()
    else:
        print("Invalid choice. Try again.")
        entrance()


def livingroom():
    print("You have entered the living room.")
    print("You see two doors.")
    print("One in front, sunlight gleams through the window.")
    print("The other is to your right, and a cold draft can be felt.")
    print("What do you want to do?")
    ans = input("1) Back to the previous room \n2) Towards the sunshine \n3) Check out the cold draft\n")

    if ans == "1":
        entrance()
    elif ans == "2":
        ljusrum()
    elif ans == "3":
        kallrum()
    else:
        print("Invalid choice. Try again.")
        livingroom()


def ljusrum():
    print("You check out the light and see a Coke Zero on the ground.")
    print("You also see a door leading to the cold room.")
    ans = input("1) Take the Coke Zero and drink it \n2) Go to the cold room\n")

    if ans == "1":
        print("You drink the Coke Zero, but it has no sugar. It tasted shit")
        print("You died. The end.")
    elif ans == "2":
        kallrum()
    else:
        print("försök igen")
        ljusrum()


def kallrum():
    print("You enter the cold room and see a normal Coke on the ground.")
    ans = input("1) Drink the Coke \n2) Go to the room with the sunshine\n")

    if ans == "1":
        print("You drink the Coke and feel refreshed. You win!")
        print("The end.")
    elif ans == "2":
        ljusrum()
    else:
        print("försök igen")
        kallrum()


print("hej detta är ett spel")
entrance()
