my_stats={
    "name":"Suhan",
    "age": 31,
    "occupation":"scientist"
}
del my_stats["age"]

my_stats["occupation"] = "CEO"

print(my_stats)
print(my_stats.get("occupation"))


my_pokemon = {
"pokemon":"Rapidash",
"type":"Fire",
"level":30
}
my_pokemon["move"]="Flame wheel"
print(my_pokemon)

for value in my_pokemon.values():
    print(value)