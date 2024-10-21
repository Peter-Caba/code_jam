import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

mario_characters = {
    'Mario': {'power_level': 8, 'max_damage': 6},
    'Luigi': {'power_level': 7, 'max_damage': 5},
    'Bowser': {'power_level': 11, 'max_damage': 9},
    'Peach': {'power_level': 6, 'max_damage': 4},
    'Toad': {'power_level': 5, 'max_damage': 3},
    'MineCraft Steve': {'power_level': 10, 'max_damage': 4},
    'Wario': {'power_level': 7, 'max_damage': 5},
    'Joker': {'power_level': 9, 'max_damage': 4}, 
    'Mega Man': {'power_level': 8, 'max_damage': 6},
    'Bowser Jr.': {'power_level': 4, 'max_damage': 3},  
    'Link': {'power_level': 7, 'max_damage': 8}, 
    'Kirby': {'power_level': 12, 'max_damage': 3},
}

your_power_level = 9
your_max_damage = 7

def print_characters():
    print('The enemy characters in the arena are:')
    for character in mario_characters.keys():
        print(character)
    print('\n')

def you_fight(character_name):
    character_health = mario_characters[character_name]['power_level']
    damage_to_character = random.randint(0, your_max_damage)
    
    if damage_to_character == 0:
        print(f'You barely miss striking {character_name}!')
    else:
        print(f'You strike {character_name}, dealing {damage_to_character} points of damage.')
    
    character_health -= damage_to_character
    mario_characters[character_name]['power_level'] = character_health  

    if character_health <= 0:
        print(f'You hit {character_name} with a final blow!')
        return True
    return False

def character_fights_you(character_name): 
    character_damage = mario_characters[character_name]['max_damage']
    damage_to_you = random.randint(0, character_damage)
    
    if damage_to_you == 0:
        print(f'{character_name} swings but misses you completely!')
    else:
        print(f'{character_name} strikes you, dealing {damage_to_you} points of damage.')
    
    global your_power_level
    your_power_level -= damage_to_you
    if your_power_level <= 0:
        print(f'You are beaten to the ground, begging for mercy from {character_name}.')
        return True
    return False

character_name = random.choice(list(mario_characters.keys()))
print(f'You find yourself in the arena with {character_name}, who has a power level of {mario_characters[character_name]["power_level"]}!')

while True:
    choice = input("Do you (e)scape, or (f)ight?: ").lower()
    
    if choice == 'e':
        print(f"You have left the arena with your life spared, leaving {character_name} waiting for the next challenger.")
        break
    elif choice == 'f':
        character_defeated = you_fight(character_name)
        if character_defeated:
            print(f'You have defeated {character_name}!')
            break
        
        you_defeated = character_fights_you(character_name)
        if you_defeated:
            break
    else:
        print("Invalid choice. Please choose '(e)' to escape or '(f)' to fight.")
        print("Thank you for playing")

