import json;

data = {}
data['characters'] = []

file = open("character_list.txt", "r")

id = 1
for line in file:
	line = line.rstrip("\n")
	characterObj = {
		'name': line,
		'id': id,
		'aliases': [line.lower()]
	}
	# Check for if this is an echo and use e as id
	if "Echo" in line:
		id -= 1
		characterObj['id'] -= 1
		characterObj['id'] = str(id) + "e"
		characterObj['aliases'][0] = characterObj['aliases'][0].replace("(echo)", "").strip()
		print(characterObj['aliases'][0])

	data['characters'].append(characterObj)
	id += 1
	
		

with open("character_list.json", "w") as data_dump:
	json.dump(data, data_dump)