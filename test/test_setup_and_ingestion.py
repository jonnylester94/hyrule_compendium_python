import os
import json
from src.setup_and_ingestion import data_ingestion, clean_creatures_data, create_valid_items_lists

def test_data_ingestion_creates_correct_directory_and_files():
    data_ingestion()
    result = os.listdir('compendium_data')
    assert result == ['monsters.json', 'materials.json', 'treasure.json', 'creatures.json', 'equipment.json']

def test_clean_creatures_removes_food_vs_non_food_categories_and_replaces_with_new_dictionary():
    clean_creatures_data()
    with open('compendium_data/creatures.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        assert 'food' not in data
        assert 'non_food' not in data
        for creature in data:
            assert 'edible' in creature
            assert creature['edible'] == 'T' or 'F'   

def test_create_valid_items_creates_correct_dictionaries():
    result = create_valid_items_lists()
    keys = ['monsters', 'creatures', 'equipment', 'materials', 'treasure']
    for key in keys:
        assert key in result
        assert type(result[key]) == list
        with open(f'compendium_data/{key}.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            for item in data:
                assert item['name'] in result[key]