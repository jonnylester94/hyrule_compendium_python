## Breath of the Wild: Hyrule Compendium

The Hyrule Compendium API (https://gadhagod.github.io/Hyrule-Compendium-API/#/) contains data on all creatures, monsters, materials, equipment, and treasure in the Nintendo Switch game The Legend of Zelda: Breath of the Wild. This Python project allows users to look up a particular item in the Compendium and receive detailed information about it. It does this by:

- using Python's requests and JSON libraries to ingest the data into 5 JSON files stored in a newly-created compendium_data directory;
- cleaning this data (specifically the creatures.json file);
- asking the user for some input (category and item); and
- if the given input is valid, returning information about that item.

The src directory contains a setup_and_ingestion file and a main script. I have tested these functions with Pytest in a separate test directory, patching the user input for the main look up function.

Feel free to clone this repo and trying looking up your favourite creatures, monsters, equipment, materials or treasures from BOTW. To setup and run:

- 1. clone the repo;
- 2. from the root directory, create a new virtual environment and activate it (python -m venv venv; source venv/bin/activate);
- 3. install the necessary project dependencies (pip install -r requirements.txt);
- 4. run the setup and ingestion file (from main directory, python src/setup_and_ingestion.py) to ingest and clean the data; and
- 5. run the main file and follow the prompts (from main directory, python src/main.py)

## Next steps/things to consider adding:

- doing more with the output - give user the option to store returned items in a database?
- constructing a series of SQL queries to interrogate/restructure new database?

