#import libs
from sys import exit

# script and version info
script = "dungeon.py"
version = "1.0.0"
author = "S Kerstetter"
created = "2020-12-05"
last_modified = "2020-12-06"

# Define player and monster stats
hp = 10
attack = 1

# THE MEAT
def boss_room(player_name, player_hp, player_attack):
    monster_dead = False

    monster_type = "orc king"
    monster_hp = 10
    monster_attack = 5

    print(f"\n\n{player_name} walks into grand hall dimly lit by torches.")
    print(f"At the head of the room is large throne with a {monster_type} sitting in it.")
    print(f"The {monster_type} speaks:")
    print(f"\t\"You've done well to make it this far, human.  You show true bravery.\"")
    print(f"\t\"The treasure here is mine and mine alone.  Leave this place now and I will spare your life.\"")

    print("\nDo you leave the dungeon?")

    choice = input("> ")

    if choice == "yes":
        print(f"The {monster_type} speaks:")
        print("\t\"You have chosen wisely, human.  Begone.\"")
        win(player_name)
    elif choice == "no":
        print(f"The {monster_type} speaks:")
        print("\t\"You are a fool.\"")
        print(f"The {monster_type} rises from the throne and draws a large axe.")
        input("\npress ENTER to continue.")
        monster_dead, player_hp = combat(player_name, player_hp, player_attack, monster_type, monster_hp, monster_attack)
    else:
        print(f"{player_name}'s reply is incoherent.")
        print(f"The {monster_type} speaks:")
        print("\t\"You are not as brave as I thought.  A coward like you does not deserve life.\"")
        print(f"The {monster_type} rises from the throne and draws a large axe.")
        input("\npress ENTER to continue.")
        monster_dead, player_hp = combat(player_name, player_hp, player_attack, monster_type, monster_hp, monster_attack)

    print(f"\n\nThe {monster_type} lies dead on the floor.  Behind them is a pile of gold!")
    print("Do you take the gold?")

    while True:
        choice = input("> ")

        if choice == "yes":
            print(f"{player_name} packs up enough gold to last a life time.")
            win(player_name)
        elif choice == "no":
            print(f"{player_name} leaves the gold.")
            print("Why did you even come down here then?!")
            win(player_name)
        else:
            print("Entry not valid.  Try again.")



def countdown_room(player_name, player_hp, player_attack):
    countdown = 3
    vines_removed = False

    print(f"\n\nAs {player_name} enters the room, they trip of a wire and hear the hiss of a burning fuse.")
    print(f"At the far end of the room is a door covered in vines.")
    print("What do you do?")

    for i in range (3):
        print(f"\nCountdown: {countdown}\n")

        choice = input("> ")

        if "remove" in choice and not vines_removed and player_attack == 5:
            print(f"{player_name} uses the sword to cut down the vines blocking the door.  The door in free of vines.")
            vines_removed = True
        elif "remove" in choice and not vines_removed and player_attack == 1:
            print(f"{player_name} clears the vines with their hands but can't completely free the door.  Continue clearing vines?")
            choice = input("> ")
            if choice == "yes":
                countdown -= 1
                print(f"\nCountdown: {countdown}\n")
                print(f"{player_name} clears the vines.  The door in now free of vines.")
                vines_removed = True
            elif choice == "no":
                print(f"{player_name} stops clearing vines.")
            else:
                print("Entry not valid.  Try again.")
        elif "explore" in choice:
            print("You see a large bomb in the corner.  Yikes!")
        elif "door" in choice and not vines_removed:
            print("Vines block the door.  Cannot open it.")
        elif "door" in choice and vines_removed:
            print(f"{player_name} opens the door and goes through it.")
            boss_room(player_name, player_hp, player_attack)
        elif "attack" in choice:
            print("Nothing to attack.")
        else:
            print("Entry not valid.  Try again.")

        countdown -= 1
        if countdown < 1:
            break

    print(f"\nCountdown: {countdown}")
    print("The room fills with a bright light as it bursts into raging flames!")
    dead(player_name)



def chest_room(player_name, player_hp, player_attack):
    skeleton_moved = False
    monster_dead = False
    sword_gone = False

    monster_type = "spooky scary skeleton"
    monster_hp = 5
    monster_attack = 5

    print("\n\nThe room is small and has no doors except the one behind you.")
    print("In the center of the room sits a chest with a skeleton lying on top of it.")
    print("What do you do?")

    while True:
        choice = input("> ")

        if "attack" in choice and not skeleton_moved:
            print("Nothing to attack.  It's just a harmless skeleton.")
        elif "attack" in choice and skeleton_moved:
            print("nothing to attack.  It's just a pile of bones.")
        elif "remove" in choice and not skeleton_moved:
            print(f"{player_name} pushes the skeleton off the chest.  The bones noisily clatter to the floor.")
            skeleton_moved = True
        elif "remove" in choice and skeleton_moved:
            print("The skeleton has already been removed.")
        elif "explore" in choice:
            print("There is nothing to explore.")
        elif "open chest" in choice and not skeleton_moved and not sword_gone:
            print("The skeleton lies on top of the chest.  Cannot open it.")
        elif "open chest" in choice and skeleton_moved and not sword_gone:
            print(f"The chest creaks as {player_name} slowly opens it.  Inside is a sword.  Do you take the sword?")
            choice = input("> ")
            if choice == "yes":
                print(f"{player_name} grabs the sword and feels way more cool!")
                player_attack = 5
                sword_gone = True
            elif choice == "no":
                print(f"{player_name} leaves the sword and closes the chest.")
            else:
                print("Entry not valid.  Try again.")
        elif "open chest" in choice and skeleton_moved and sword_gone:
            print("The chest is empty.")
        elif "door" in choice and not skeleton_moved and not monster_dead:
            print(f"{player_name} turns around and goes back through the door.")
            split_room(player_name, player_hp, player_attack)
        elif "door" in choice and skeleton_moved and not monster_dead:
            print(f"{player_name} turns their back on the room and walks to the door.")
            print("Noisy clattering fills the chamber.")
            print(f"{player_name} turns back toward the room and sees a {monster_type} reassemble itself.")
            input("\npress ENTER to continue.")
            monster_dead, player_hp = combat(player_name, player_hp, player_attack, monster_type, monster_hp, monster_attack)
            print("What do you do?")
        elif "door" in choice and skeleton_moved and monster_dead:
            print(f"{player_name} opens the door and goes through it.")
            split_room(player_name, player_hp, player_attack)
        else:
            print("Entry not valid.  Try again.")



def split_room(player_name, player_hp, player_attack):
    monster_dead = False
    monster_type = "large spider"
    monster_hp = 3
    monster_attack = 1

    print("\n\nThe room is very dark. In the distance you see the outline of a door.  You get the creeping feeling that something is watching you but you see no living thing in the gloom.")
    print("What do you do?")

    while True:
        choice = input("> ")

        if "attack" in choice:
            print(f"{player_name} wildly swings about but hits nothing.")
        elif "explore" in choice:
            print(f"{player_name} carefully works around the edges of the dark room and finds another door.  Do you go through the door?")
            choice = input("> ")
            if choice == "yes":
                print(f"{player_name} opens the door and goes through.")
                chest_room(player_name, player_hp, player_attack)
            elif choice == "no":
                print(f"{player_name} turns around and walks back into the middle of the dark room.")
            else:
                print("Entry not valid.  Try again.")
        elif "door" in choice and not monster_dead:
            print(f"{player_name} slowly walks toward the door...")
            print(f"A {monster_type} suddenly drops out of the darkness above!")
            input("\npress ENTER to continue.")
            monster_dead, player_hp = combat(player_name, player_hp, player_attack, monster_type, monster_hp, monster_attack)
            print("What do you do?")
        elif "door" in choice and monster_dead:
            print(f"{player_name} opens the door and goes through.")
            countdown_room(player_name, player_hp, player_attack)
        elif "remove" in choice:
            print("Nothing blocks your way.")
        else:
            print("Entry not valid.  Try again.")



def blocked_room(player_name, player_hp, player_attack):
    rubble_moved = False

    print("\n\nThe room is long and narrow.  At the end of the room is door.  The walls seem unstable.")
    print("It seems at somepoint part of the roof collpased in and rubble blocks the door.")
    print("What do you do?")

    while True:
        choice = input("> ")

        if "attack" in choice:
            print("There is nothing to attack.")
        elif "explore" in choice:
            print("You look around the room but see nothing of interest.")
        elif "door" in choice and not rubble_moved:
            print("Rubble blocks the door.  Cannot open it.")
        elif "door" in choice and rubble_moved:
             print(f"{player_name} opens the door and walks through.")
             split_room(player_name, player_hp, player_attack)
        elif "remove" in choice:
            print(f"{player_name} digs into the rubble and moves it away from the door.  The door is clear now.")
            rubble_moved = True



def start_room(player_name, player_hp, player_attack):
    monster_type = "rat"
    monster_hp = 2
    monster_attack = 1

    monster_dead = False

    print(f"\n\nOnce upon a time, {player_name} entered a dark dungeon...")
    print(f"In front of you is a door.  A {monster_type} is between you and the door.  What do you do?")

    while True:
        choice = input("> ")

        if "attack" in choice and not monster_dead:
            monster_dead, player_hp = combat(player_name, player_hp, player_attack, monster_type, monster_hp, monster_attack)
            print("What do you do?")
        elif "attack" in choice and monster_dead:
            print(f"{player_name} dissects the {monster_type} with all the care of a middle school biology experiment.")
        elif "explore" in choice and not monster_dead:
            print(f"{player_name} tries to explore but the {monster_type} attacks.")
            input("\npress ENTER to continue.")
            monster_dead, player_hp = combat(player_name, player_hp, player_attack, monster_type, monster_hp, monster_attack)
            print("What do you do?")
        elif "explore" in choice and monster_dead:
            print("There is another door behind you. Do you go through it?")
            choice = input("> ")
            if "yes" in choice:
                win(player_name)
            elif "no" in choice:
                print(f"{player_name} turn away from the door.")
            else:
                print("Entry not valid. Try again.")
        elif "door" in choice and not monster_dead:
            print(f"The {monster_type} blocks the door.  Cannot open it.")
        elif "door" in choice and monster_dead:
            print(f"{player_name} opens the door and goes through.")
            blocked_room(player_name, player_hp, player_attack)
        elif "remove" in choice:
            print("Nothing blocks your way.")
        else:
            print("Entry not valid.  Try again.")



def dead(player_name):
    print(f"{player_name} perished in the dark depths of the dangerous dungeon.")
    print("I wish you better luck in your next life.")
    exit(0)



def win(player_name):
    print(f"{player_name} walks out of the dungeon into sunlight and lives happily ever after.")
    print("The End.")
    exit(0)



def combat(player_name, player_hp, player_attack, monster_type, monster_hp, monster_attack):
    print(f"\nThe {monster_type} approaches.")
    while True:
        input(f"\nPress ENTER for {player_name}'s attack.\n")
        monster_hp -= player_attack
        print(f"{player_name} swings with all their might.")
        print(f"The {monster_type} takes {player_attack} damage.")
        if monster_hp <=0:
            print(f"\nThe {monster_type} is defeated!")
            return True, player_hp

        input(f"\nPress ENTER for the {monster_type}'s attack.\n")
        player_hp -= monster_attack
        print(f"The {monster_type} lunges at you!")
        print(f"{player_name} takes {monster_attack} damage.")
        if player_hp <= 0:
            print(f"\n{player_name} has no more HP.\n")
            dead(player_name)



#Game introduction, display version info, collect player name, and start game
print(f"""
DUNGEON CRAWL

In this game you must escape from the dungeon OR DIE TRYING!

Credits
Script: {script}
Date Created: {created}
Author: {author}
Version: {version}
Last Modified = {last_modified}
""")

print("What is your name?")
name = input("> ")

print(f"Welcome to Dungeon Crawl, {name}!")
print("""
Throuhgout the game you will receive prompts to type in commands.
Acceptable commands are:
\tdoor - to open a door.
\texplore - to explore your surrounds.
\tattack - to engage in combat.
\tremove - to remove objects from your path.
\topen chest - to open treasure chests.
\tyes and no - to answer yes/no questions.

Please use lowercase when entering commands.
""")

input("press ENTER to continue.")

start_room(name, hp, attack)
