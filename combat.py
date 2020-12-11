import random

# player stats and inventory
player = {
    'name' : 'Scooteth',
    'hp' : 10,
    'weapon' : 'fist'
}

# dict of weapons and attack power
weapons_list = {
    'fist' : [1,2],
    'sword' : [3,5]
}

# nested dicts of monsters and their stats
bestiary = {
    'rat' : {
        'name' : 'rat',
        'hp' : 2,
        'attack' : [1,2]
    },
    'large spider' : {
        'name' : 'large spider',
        'hp' : 3,
        'attack' : [1,3]
    },
    'spooky scary skeleton' : {
        'name' : 'spooky scary skeleton',
        'hp' : 5,
        'attack' : [3,5]
    }
}


# randomly select monster type from bestiary
monster_list = list(bestiary.items())
rand_monster = random.choice(monster_list)
monster_type = rand_monster[1].get('name')


def dead(player):
    print(f"{player['name']} perished in the dark depths of the dangerous dungeon.")
    print("I wish you better luck in your next life.")
    exit(0)


def combat(player, monster_type, weapons_list, bestiary):
    # unpack monster from bestiary
    monster = bestiary[monster_type]

    print(f"\nThe {monster['name']} approaches.")

    while True:
        # player's turn
        input(f"\nPress ENTER for {player['name']}'s attack.\n")
        print("monster HP before attack: ", monster['hp'])  # remove
        # calculate player attack value
        player_attack = random.randint(weapons_list[player['weapon']][0], weapons_list[player['weapon']][1])
        print("calulated player_attack: ", player_attack)   # remove
        monster['hp'] -= player_attack
        print(f"{player['name']} swings their {player['weapon']} with all their might.")
        print(f"The {monster['name']} takes {player_attack} damage.")
        print("monster HP after attack: ", monster['hp'])   # remove
        if monster['hp'] <=0:
            print(f"\nThe {monster['name']} is defeated!")
            return True, player

        # monster's turn
        input(f"\nPress ENTER for the {monster['name']}'s attack.\n")
        print("player HP before attack: ", player['hp'])   # remove
        # calculate monster attack value
        monster_attack = random.randint(monster['attack'][0], monster['attack'][1])
        print("calculated monster attack: ", monster_attack)   # remove
        player['hp'] -= monster_attack
        print(f"The {monster['name']} lunges at you!")
        print(f"{player['name']} takes {monster_attack} damage.")
        print("player HP after attack: ", player['hp'])   # remove
        if player['hp'] <= 0:
            print(f"\n{player['name']} has no more HP.\n")
            dead(player)

combat(player, monster_type, weapons_list, bestiary)
