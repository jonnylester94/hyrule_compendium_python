import requests
import json
import os

link = 'https://botw-compendium.herokuapp.com/api/v2'

categories = ['creatures', 'equipment', 'materials', 'monsters', 'treasure']

def data_ingestion():
    ''' Uses the requests & JSON libraries to write the data from the API to five distinct JSON files in a new compendium_data dir, one file per category. '''
    response = requests.get(link)
    json_result = response.json()

    if not os.path.exists('compendium_data'):
        os.mkdir('compendium_data')

    for item in categories:
        with open(f'compendium_data/{item}.json', 'w', encoding='utf-8') as f:
            content = json_result['data'][item]
            f.write(json.dumps(content))

def clean_creatures_data():
    ''' Cleans the creatures.json file by removing the food and non_food sub categories and instead adding a new dictionary to each item in the form 'edible: T / F. Combines into one list and overwrites the existing json. '''

    with open('compendium_data/creatures.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        edible = data['food']
        non_edible = data['non_food']
        for creature in edible:
            creature['edible'] = 'T'
        for creature in non_edible:
            creature['edible'] = 'F'

        with open('compendium_data/creatures.json', 'w', encoding='utf-8') as f:
            content = edible + non_edible
            f.write(json.dumps(content))

def create_valid_items_lists() -> dict:
    ''' Goes through the files in the compendium_data directory to create a dictionary of valid lists for each category so that the user cannot input an invalid choice. Returns data in format: {'creatures': [list_of_creatures], 'equipment': [list_of_equipment], 'materials': [list_of_materials], 'monsters': [list_of_monsters], 'treasure': [list_of_treasure]} '''

    valid_items = {}
    for file in os.listdir('compendium_data'):
        category_name = file[:-5]
        with open(f'compendium_data/{file}', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            valid = [item['name'] for item in data]
            valid_items[category_name] = valid

    return valid_items


data_ingestion()
clean_creatures_data()
create_valid_items_lists()