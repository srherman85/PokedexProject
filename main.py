from flask import Flask, request, render_template
import requests
import os
import random

app = Flask(__name__)

# Optionally configure static file serving behavior
app.static_url_path = '/custom_static'  # Change the URL prefix for static files
app.static_folder = 'static'  # Specify the folder containing static files


def capitalize_first_letters(words):
    return ' '.join(word.capitalize() for word in words.split())


def get_number_from_name(name):
    try:
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
        self.image_url = None

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
            self.name = data['forms'][0]['name'].capitalize()
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
                self.stats[capitalize_first_letters(stat_name)] = base_stat

            # Fetching image URL
            self.image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{self.number}.png"
            print(self.image_url)

            # Download and save image
            self.download_image()

        except Exception as e:
            print(f"Invalid ID.")
            exit()

    def download_image(self):
        if self.image_url:
            try:
                response = requests.get(self.image_url)
                if response.status_code == 200:
                    # Create 'static/images' folder if it doesn't exist
                    os.makedirs('static/images', exist_ok=True)
                    # Save image to 'static/images' folder with the pokemon number as filename
                    with open(f'static/images/{self.number}.png', 'wb') as f:
                        f.write(response.content)
                    print("Image downloaded successfully.")
                else:
                    print("Failed to download image:", response.status_code)
            except Exception as e:
                print("Error downloading image:", e)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pokemon_number = request.form['pokemon_number']
        if pokemon_number.lower() == 'random':
            pokemon_number = str(random.randint(1, 1026))
        pokemon = Pokemon(pokemon_number)
        return render_template('index.html', pokemon=pokemon, pokemon_number=pokemon_number)
    return render_template('index.html', pokemon=None, pokemon_number=None)


if __name__ == "__main__":
    app.run(debug=True)
