import pokebase as pb

count = pb.APIResourceList('pokemon-species').count

f = open('pokemon_de.txt', 'a+')

for i in range(1, count + 1):
    pokemon = pb.pokemon_species(i)
    for name in pokemon.names:
        if name.language.name == 'de':
            print(name.name.lower())
            f.write(name.name.lower())
            f.write('\n')

f.close()
