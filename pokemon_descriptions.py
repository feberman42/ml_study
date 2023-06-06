import pokebase as pb

count = pb.APIResourceList('pokemon-species').count

f = open('pokemon_flavor_en.txt', 'w+')
data = []
for i in range(1, count + 1):
    pokemon = pb.pokemon_species(i)
    for entry in pokemon.flavor_text_entries:
        if entry.language.name == 'en':
            print(i, pokemon.name)
            text = entry.flavor_text.lower()
            text = text.replace(',','')
            text = text.replace('.','')
            text = text.replace(' m ', ' meters ')
            text = text.replace('\r', ' ')
            text = text.replace('\n', ' ')
            text = text.replace('\f', ' ')
            text = text.replace('“', '')
            text = text.replace('”', '')
            text = text.replace('!', '')
            text = text.replace('  ', ' ')
            data.append(text)

data = set(data)
for i in data:
	f.write(i)
	f.write('\n')
f.close()
