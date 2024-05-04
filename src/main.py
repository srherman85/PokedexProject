from flask import Flask, request, render_template, redirect, url_for
import requests
import os
import json
import random
from builtins import enumerate


app = Flask(__name__)

# Optionally configure static file serving behavior
app.static_url_path = '/custom_static'  # Change the URL prefix for static files
app.static_folder = 'static'  # Specify the folder containing static files


def capitalize_first_letters(words):
    return ' '.join(word.capitalize() for word in words.split())


def get_number_from_name(name):
    try:
        # If it contains a space, edit the name:
        if " " in name:
            name = name.replace(" ", "-")

        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        data = response.json()
        return data['id']
    except Exception as e:
        print(f"Error retrieving Pokémon number from name: {e}")
        return 0  # Return 0 if unable to retrieve number


class Pokemon:
    def __init__(self, name_or_number):
        if name_or_number.isdigit() and name_or_number.isnumeric():
            self.number = str(name_or_number)
        else:
            self.number = str(get_number_from_name(name_or_number.lower()))
        self.name = None
        self.modified_name = None
        self.types = []
        self.abilities = {}
        self.stats = {}
        self.fetch_data()

    def fetch_data(self):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{self.number}"
            response = requests.get(url)
            data = response.json()

            # Fetching types
            types_data = data['types']
            for type_info in types_data:
                self.types.append(type_info['type']['name'])
            self.types = [capitalize_first_letters(t) for t in self.types]

            # Fetching abilities and their short effects
            abilities_data = data['abilities']
            for ability_info in abilities_data:
                ability_name = capitalize_first_letters(ability_info['ability']['name'])
                if '-' in ability_name:
                    ability_name = ability_name.replace('-', " ")
                    for word in ability_name:
                        ability_name = capitalize_first_letters(ability_name)

                ability_url = ability_info['ability']['url']

                # Fetch ability data
                ability_response = requests.get(ability_url)
                ability_data = ability_response.json()

                # Find the flavor text with language 'en'
                flavor_text_en = next((entry['flavor_text'] for entry in ability_data['flavor_text_entries'] if
                                       entry['language']['name'] == 'en'), None)
                if flavor_text_en:
                    self.abilities[ability_name] = flavor_text_en

            # Ensure only unique types and abilities
            self.types = list(set(self.types))

            # Ensure at most 3 abilities
            self.abilities = {k: self.abilities[k] for k in list(self.abilities)[:3]}

            # Name
            self.name = data['species']['name'].capitalize()
            if '-' in self.name:
                self.modified_name = self.name.replace('-', " ")
                for word in self.modified_name:
                    self.modified_name = capitalize_first_letters(self.modified_name)
            else:
                self.modified_name = self.name

            # Fetching stats
            stats_data = data['stats']
            for stat_info in stats_data:
                stat_name = stat_info['stat']['name']
                base_stat = stat_info['base_stat']
                formatted_stat_name = format_stat_name(stat_name)
                self.stats[formatted_stat_name] = base_stat

        except Exception as e:
            print(f"Invalid ID.")
            exit()


def format_stat_name(stat_name):
    formatted_names = {
        'hp': 'HP',
        'attack': 'Atk',
        'defense': 'Def',
        'special-attack': 'SpAtk',
        'special-defense': 'SpDef',
        'speed': 'Spd'
    }
    return formatted_names.get(stat_name.lower(), stat_name.capitalize())

# SimplePokemon, which only uses name and display_name. This
# allows the "Teamlist" route to load a lot faster, since it does
# not have to worry about all the other attributes.
class SimplePokemon:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.display_name = name

        if '-' in self.display_name:
            self.display_name = self.display_name.replace('-', " ")
            self.display_name = capitalize_first_letters(self.display_name)
        else:
            self.display_name = capitalize_first_letters(self.display_name)

    def fetch_name_from_api(self):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{self.number}"
            response = requests.get(url)
            data = response.json()
            return data['species']['name'].capitalize()
        except Exception as e:
            print(f"Error retrieving Pokémon name from API: {e}")
            return ""  # Return an empty string if unable to retrieve the name



    def fetch_data(self):
        # Since we're only interested in name and number, we can skip fetching other data
        pass


@app.route('/pokemon_details/<pokemon_number>')
def pokemon_details(pokemon_number):
    # Ensure pokemon_number is a string
    pokemon_number = str(pokemon_number)
    pokemon = Pokemon(pokemon_number)
    return render_template('pokemon_details.html', pokemon=pokemon)


@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon = None  # Initialize pokemon variable
    error_message = None  # Initialize error message

    if request.method == 'POST':
        pokemon_number = request.form['pokemon_number']

        # Check if the form submission is empty
        if not pokemon_number.strip():
            error_message = "Please enter a Pokemon name or Pokedex number."
        else:
            if pokemon_number.lower() == 'r':
                pokemon_number = str(random.randint(1, 1026))

            # Validate the Pokemon number by making a request to the PokeAPI
            if is_valid_pokemon_number(pokemon_number):
                return redirect(url_for('pokemon_details', pokemon_number=pokemon_number))
            else:
                error_message = "Invalid Pokemon number. Please enter a valid Pokemon name or Pokedex number."

    return render_template('index.html', pokemon=pokemon, error_message=error_message)

def is_valid_pokemon_number(pokemon_number):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}')
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking Pokemon number: {e}")
        return False

def get_number_from_name(name):
    try:
        if " " in name:
            name = name.replace(" ", "-")

        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)
        data = response.json()
        return data['id']
    except Exception as e:
        print(f"Error retrieving Pokémon number from name: {e}")
        return 0  # Return 0 if unable to retrieve number

if __name__ == "__main__":
    app.run(debug=True)
