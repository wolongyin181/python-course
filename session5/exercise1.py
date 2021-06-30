pokemon_list=['pikachu','Eevee','Snorlax','Charmander','Charizard']
my_team=['Landorus', 'Weedle', 'Spearow', 'Pidgey', 'Gardevoir']

pokemon_list.remove('pikachu')
pokemon_list.pop(0)
print(pokemon_list)

pokedex=pokemon_list+my_team


pokedex.insert(3,'Rattata')
print(pokedex)
print(len(pokedex))

for a in pokedex:
    print(a)

if 'Charizard' in pokedex:
    print('Charizard is in pokedex')