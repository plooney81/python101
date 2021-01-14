import json

with open('locations.json', 'r') as file_handle:
    digitalCrafts = json.load(file_handle)

    for country in digitalCrafts:
        for region in digitalCrafts[country]:
            print(f'{country} : {region} : {digitalCrafts[country][region]}')

new_country = input('New Country? ')
new_city = input('New City? ')
new_building = input('New Building?')

digitalCrafts[new_country] = {
    new_city: new_building
}

with open('locations.json', 'w') as file_handle:
    json.dump(digitalCrafts, file_handle)