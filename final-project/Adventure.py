import random

character_stats = {
'attack': 10,
'health': 50,
}
monster_stats = {
'name' :"pikeman",
'attack': 10,
'health': 60
}

monster_dict = [
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
        'name': "Minotaur",
        'attack':14,
        'health':50
    },
    {
        'name': "Ogre",
        'attack':13,
        'health':40
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
        'name': "Manitocore",
        'attack':13,
        'health':80
    },
    {
        'name': "Cyclops",
        'attack':15,
        'health':70
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
        'name': "Ghost dragon",
        'attack':19,
        'health':180
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

def new_game():

    travel_distance=500

    print("Welcome to the adventure.")
    input()

    while travel_distance>0:
        print(f"Capital is {travel_distance}km away. Please decide how long you want to travel today.")
        daily_distance=int(input("Please input a number between 10-50."))
        
        if (daily_distance>=10 and daily_distance<=50):
            travel_distance=travel_distance - daily_distance
            new_move()
        else:
            print("Sorry, please try again.")
            continue  
    else:
        print("Congratulations, you arrived at Capital in safety. You completed the challenge!")

def new_move():

    event=random.randint(2,2)

    if event == 1:
        print("It's almost dawn now. You decide to find a place to stay for the night.\nA monster suddenly appears in front of you. Although you are tired, you have no choice but to fight.")
        input()
        new_fight()
    elif event == 2:
        print ("It's almost dawn now. You decide to find a place to stay for the night.\nYou see the light from a village nearby. You know you will have a good rest tonight.")
        input()
    elif event == 3:
        print("It's almost dawn now. You decide to find a place to stay for the night.\nSuddenly you see a witch's hut in the mist, you decide to visit the hut. The witch presents you a number of items you can buy with gold.")
        input()

def new_fight():

    while monster_stats['health']>0 and character_stats['health']>0:
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
        end_fight()

def attack():
    character_attack=character_stats['attack']
    character_health=character_stats['health']
    monster_attack=monster_stats['attack']
    monster_health=monster_stats['health']

    event=random.randint(1,3)

    if event == 1:
        monster_health=monster_health - character_attack
        monster_stats['health'] = monster_health
        print(f'You hit the monster! Your health is {character_health}, monster health is {monster_health}')
        input()
    elif event == 2:
        print (f'You missed the monster! Your health is {character_health}, monster health is {monster_health}')
        input()
    elif event == 3:
        character_health=character_health-monster_attack
        character_stats['health']=character_health
        print (f'You are hit by the monster! Your health is {character_health}, monster health is {monster_health}')
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
    print(f'Here is your stats. Your health is {character_health}, your attack is {character_attack}, monster health is {monster_health}, monster attack is {monster_attack}.')


def end_fight():
    
    if (monster_stats['health']<=0 and character_stats['health']>0):
        print("Congratulations, you win the fight!")
    elif(monster_stats['health']>0 and character_stats['health']<=0):
        print("You lost the fight. You are unable to continue the journey. But don't worry, other warriors will protect the queen.")


start_game = input("My warrior, our homeland is on fire.\nQueen has decided to travel back to the capital and stand with her people.\nWe need your help to protect the queen on her journey back home.\nMy warrior, on the journey you will encounter monsters sent by enermies. You will have to fight, you may be injured, and you may even die.\nMy warrior, do you dare to accept this challenge?\ny/n/end")

if(start_game == 'y'):
    new_game()
elif(start_game == 'n'):
    print("OK, let me know when you change your mind.")
elif(start_game == 'end'):
    quit()
else:
    print("Error input, please restart.")

