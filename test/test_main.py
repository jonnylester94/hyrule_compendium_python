from unittest.mock import patch
from src.main import look_up

# test example monster
@patch('builtins.input', side_effect=['monster', 'blue moblin'])
def test_look_up_returns_correct_info_about_monsters_item_in_compendium(mock_input):
    result = look_up()
    assert result == {'category': 'monsters', 'common_locations': ['Hyrule Field', 'Deep Akkala'], 'description': "These heavyweight monsters can be found all over Hyrule. They're much tougher than their standard counterparts and often have much stronger weapons equipped.", 'drops': ['moblin horn', 'moblin fang', 'moblin guts'], 'id': 109, 'image': 'https://botw-compendium.herokuapp.com/api/v2/entry/blue_moblin/image', 'name': 'blue moblin'}

# test example creature
@patch('builtins.input', side_effect=['creature', 'maraudo wolf'])
def test_look_up_returns_correct_info_about_creatures_item_in_compendium(mock_input):
    result = look_up()
    assert result == {"category": "creatures", "common_locations": ["Tabantha Frontier", "Great Hyrule Forest"], "description": "These wolves are not only carnivorous but can also be downright fierce. They're highly aggressive and aren't afraid to attack people. They hunt in groups and surround their prey as a means of bringing it down. That said, if one of their own is injured, the rest are wise enough to run away. They communicate via howls, so if you're wandering the forest and hear their call, you had best take care.", "drops": ["raw prime meat", "raw gourmet meat"], "id": 21, "image": "https://botw-compendium.herokuapp.com/api/v2/entry/maraudo_wolf/image", "name": "maraudo wolf", "edible": "F"}
    
# test example equipment
@patch('builtins.input', side_effect=['equipment', 'mighty lynel spear'])
def test_look_up_returns_correct_info_about_equipment_item_in_compendium(mock_input):
    result = look_up()
    assert result == {"attack": 20, "category": "equipment", "common_locations": ["Great Hyrule Forest", "Deep Akkala"], "defense": 0, "description": "The weight and cutting edge of this Lynel-made spear have both been enhanced. It's immensely heavy for a Hylian, but a Lynel can cleave through rock with a single swing.", "id": 321, "image": "https://botw-compendium.herokuapp.com/api/v2/entry/mighty_lynel_spear/image", "name": "mighty lynel spear"}

# test example material
@patch('builtins.input', side_effect=['material', 'silent princess'])
def test_look_up_returns_correct_info_about_materials_item_in_compendium(mock_input):
    result = look_up()
    assert result == {"category": "materials", "common_locations": ["Hyrule Ridge", "West Necluda"], "cooking_effect": "stealth up", "description": "This lovely flower was said to have been a favorite of the princess of Hyrule. Once feared to have gone extinct, it's recently been spotted growing in the wild.", "hearts_recovered": 0, "id": 199, "image": "https://botw-compendium.herokuapp.com/api/v2/entry/silent_princess/image", "name": "silent princess"}

# test example treasure
@patch('builtins.input', side_effect=['treasure', 'luminous ore deposit'])
def test_look_up_returns_correct_info_about_treasure_item_in_compendium(mock_input):
    result = look_up()
    assert result == {"category": "treasure", "common_locations": ["Greater Hyrule"], "description": "This deposit contains quite a bit of luminous stone. Crack it open to get at the easily process rocks within.", "drops": ["luminous", "flint"], "id": 389, "image": "https://botw-compendium.herokuapp.com/api/v2/entry/luminous_ore_deposit/image", "name": "luminous ore deposit"}
