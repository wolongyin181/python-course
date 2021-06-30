import random

#nested list to store data of character and monster
character_stats = {
'attack': 10,
'health': 100,
}
monster_stats = {
'name' :"",
'attack': 0,
'health': 0
}

#A list of monsters is available which will be randomly selected and insert into monster_stats
monster_dict = [
    {
        'name': "Gargoyle",
        'attack': 6,
        'health': 16,
    },    
    {
        'name': "Medusa",
        'attack': 9,
        'health': 25,
    },
    {
        'name': "Lich",
        'attack':13,
        'health':30
    },
    {
        'name': "Basilisk",
        'attack':11,
        'health':35
    },
    {
        'name': "Ogre",
        'attack':13,
        'health':40
    },
    {
        'name': "Minotaur",
        'attack':14,
        'health':50
    },
    {
        'name': "Thunderbird",
        'attack':13,
        'health':60
    },
    {
        'name': "Wyvern",
        'attack':14,
        'health':70
    },
    {
        'name': "Cyclops",
        'attack':15,
        'health':70
    },
    {
        'name': "Manitocore",
        'attack':13,
        'health':80
    },
    {
        'name': "Naga",
        'attack':16,
        'health':110
    },
    {
        'name': "Black knight",
        'attack':16,
        'health':120
    },
    {
        'name': "Firebird",
        'attack':18,
        'health':150
    },    
    {
        'name': "Behemoth",
        'attack':17,
        'health':160
    },
    {
        'name': "Hydra",
        'attack':16,
        'health':175
    },
    {
        'name': "Gold dragon",
        'attack':27,
        'health':250
    },
    {
        'name': "Black dragon",
        'attack':25,
        'health':300
    },
    {
        'name': "Titan",
        'attack':24,
        'health':300
    }
    ]

#variable to store data from functions
distance = [500]
heal_portion = [0]

#select a distance between 10-50 to travel. Total distance needs to travel is 500km.
#If data input outside the range will ask to try again.
def new_game():

    travel_distance=500

    print("Welcome to the adventure.")
    input()

    while travel_distance>0:
        print(f"Capital is {travel_distance}km away. Please decide how long you want to travel today.")
        daily_distance=int(input("Please input a number between 10-50."))
        
        if (daily_distance>=10 and daily_distance<=50):
            travel_distance=travel_distance - daily_distance
            distance[0]=travel_distance
            new_move()
        else:
            print("Sorry, please try again.")
            continue  
    else:
        print("You arrived at Capital in safety. Congratulations, you completed the challenge!")
    return travel_distance

#for each day's travel, randomly decide an event to happen
#event = 1 is fight with monster
#event = 2 is nothing happens
#event = 3 is get a heal portion
def new_move():

    event=random.randint(1,3)

    if event == 1:
        new_fight()
        input()
    elif event == 2:
        nothing_happens()
        input()
    elif event == 3:
        given_heal_portion()
        input()

#randomly define the monster to fight with, strength of monster depends on travel distance, longer travelled, stronger the monster
#two options to choose: attack and view stats
def new_fight():
    if (distance[0]<500 and distance[0] >=375):
        monster_number=random.randint(0,4)
    elif (distance[0]<375 and distance[0] >=250):
        monster_number=random.randint(4,9)
    elif (distance[0]<250 and distance[0] >=125):
        monster_number=random.randint(9,14)
    elif (distance[0]<125 and distance[0] >=0):
        monster_number=random.randint(14,18)   

    monster_stats['name']=monster_dict[monster_number]['name']
    monster_stats['attack']=monster_dict[monster_number]['attack']
    monster_stats['health']=monster_dict[monster_number]['health']
    
    monster_name=monster_stats['name']

    print(f"It's almost dawn now. You decide to find a place to stay for the night.\nA {monster_name} suddenly appears in front of you. Although you are tired, you have no choice but to fight.")

    while monster_stats['health']>0:
        if (character_stats['health']>0):
            choose_option = int(input("Please select from the following options: 1. Attack; 2. View stats."))
      
            if (choose_option == 1):
                attack()
                continue
            elif (choose_option == 2):
                view_stats()
                continue
            else:
                print("Sorry, please select from menu.")
                continue
        else:
            near_death()
    else:
        end_fight()

def nothing_happens():
    print ("It's almost dawn now. You decide to find a place to stay for the night.\nYou see the light from a village nearby. You know you will have a good rest tonight.")

#being given a heal portion, number of heal portions can accumulate
def given_heal_portion():
    heal_portion[0]=heal_portion[0]+1
    heal_portion_number=heal_portion[0]
    print(f"It's almost dawn now. You decide to find a place to stay for the night.\nA shepherd showed you the direction to the closest village. Before he disappears, he also gives you some heal portion. You have {heal_portion_number} heal portion now.")

#when select attack, randomly decide one of the three events: hit, miss, been hit
def attack():
    character_attack=character_stats['attack']
    character_health=character_stats['health']
    monster_name=monster_stats['name']
    monster_attack=monster_stats['attack']
    monster_health=monster_stats['health']

    event=random.randint(1,3)

    if event == 1:
        monster_health=monster_health - character_attack
        monster_stats['health'] = monster_health
        print(f'You hit the {monster_name}! Your health is {character_health}, {monster_name} health is {monster_health}')
        input()
    elif event == 2:
        print (f'You missed the {monster_name}! Your health is {character_health}, {monster_name} health is {monster_health}')
        input()
    elif event == 3:
        character_health=character_health-monster_attack
        character_stats['health']=character_health
        print (f'You are hit by the {monster_name}! Your health is {character_health}, {monster_name} health is {monster_health}')
        input()

    character_attack=character_stats['attack']
    character_health=character_stats['health']
    monster_attack=monster_stats['attack']
    monster_health=monster_stats['health']

def view_stats():
    character_attack=character_stats['attack']
    character_health=character_stats['health']
    monster_attack=monster_stats['attack']
    monster_health=monster_stats['health']
    monster_name=monster_stats['name']
    print(f'Here is your stats. Your health is {character_health}, your attack is {character_attack}, {monster_name} health is {monster_health}, {monster_name} attack is {monster_attack}.')

#when win a fight, attack+1, health back to 100
def end_fight():
    
    if (monster_stats['health']<=0 and character_stats['health']>0):
        character_stats['attack'] = character_stats['attack']+1
        character_stats['health'] = 100
        character_attack=character_stats['attack']
        character_health=character_stats['health']
        print(f"Congratulations, you win the fight! You are getting stronger! Character attack +1. Your new attack is {character_attack}. After a night of rest, you also fully recover. Your new health is {character_health}.")

#when health<0 at any time during a fight, function to ask for using heal portion to +20 HP
#if no heal portion is available -> game ends.
def near_death():
    heal_portion_number=heal_portion[0]
    if (heal_portion_number>0):
        print(f"You are badly injured! You have {heal_portion_number} heal portions.")
        heal=input("Do you want to use one?y/n")

        if (heal == 'y'):
            heal_portion[0]=heal_portion[0]-1
            character_stats['health']=character_stats['health']+20
            character_health=character_stats['health']
            print(f"The portion works! Your new health is {character_health}.")
        elif (heal == 'n'):
            print("You lose the fight. Don't worry, other warriors will protect the queen to Capital.")
            quit()
    else:
        print("You lose the fight. Don't worry, other warriors will protect the queen to Capital.")
        quit()


start_game = input("My warrior, our homeland is on fire.\nQueen has decided to travel back to the capital and stand with her people.\nWe need your help to protect the queen on her journey back home.\nMy warrior, on the journey you will encounter monsters sent by enermies. You will have to fight, you may be injured, and you may even die.\nMy warrior, do you dare to accept this challenge?\ny/n/end")

if(start_game == 'y'):
    new_game()
elif(start_game == 'n'):
    print("OK, let me know when you change your mind.")
elif(start_game == 'end'):
    quit()
else:
    print("Error input, please restart.")

