import random


# dict of weapons and attack power
weapons_list = {
    'fist' : {'min': 1, 'max': 2},
    'sword' : {'min': 3, 'max': 5}
}

player = {
    'name' : 'Scooteth',
    'hp' : 10,
    'weapon' : 'fist'
}

# damage calculator for combat
for i in range (6):
    #print(random.randint(weapons_list[player['weapon']][0], weapons_list[player['weapon']][1]))
    print(random.randint(weapons_list[player['weapon']]['min'], weapons_list[player['weapon']]['max']))
