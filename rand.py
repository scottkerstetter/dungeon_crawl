import random

bestiary = {
    'rat' : {
        'name' : 'rat',
        'hp' : 2,
        'attack' : 1
    },
    'large spider' : {
        'name' : 'large spider',
        'hp' : 3,
        'attack' : 1
    },
    'spooky scary skeleton' : {
        'name' : 'spooky scary skeleton',
        'hp' : 5,
        'attack' : 5
    }
}

monster_list = list(bestiary.items())
rand_monster = random.choice(monster_list)
monster_type = rand_monster[1].get('name')
print("monster_type: ", monster_type)
