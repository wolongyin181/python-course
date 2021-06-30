    if (distance[0]<500 and distance[0] >=375):
        monster_number=random.randint(0,4)
    elif (distance[0]<375 and distance[0] >=250):
        monster_number=random.randint(4,9)
    elif (distance[0]<250 and distance[0] >=125):
        monster_number=random.randint(9,14)
    elif (distance[0]<125 and distance[0] >=0):
        monster_number=random.randint(14,18)