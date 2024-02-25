import requests
import json


class Pokemon:
    def __init__(self, number):
        self.number = number
        self.name = None
        self.types = []
        self.abilities = {}
        self.stats = {}
        self.fetch_data()

    def fetch_data(self):
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{self.number.lower()}"
            response = requests.get(url)
            data = response.json()

            # Fetching types
            types_data = data['types']
            for type_info in types_data:
                self.types.append(type_info['type']['name'])

            # Fetching abilities and their short effects
            abilities_data = data['abilities']
            for ability_info in abilities_data:
                ability_name = ability_info['ability']['name']
                ability_url = ability_info['ability']['url']
                ability_response = requests.get(ability_url)
                ability_data = ability_response.json()
                ability_effect = ability_data['effect_entries'][0]['short_effect']
                self.abilities[ability_name] = ability_effect  # Store as dictionary

            # Ensure only unique types and abilities
            self.types = list(set(self.types))
            self.abilities = list(set(self.abilities))

            # Ensure at most 3 abilities
            self.abilities = self.abilities[:3]

            # Name
            self.name = data['forms'][0]['name']

            # Number
            self.number = data['id']

            # Fetching stats
            stats_data = data['stats']
            for stat_info in stats_data:
                stat_name = stat_info['stat']['name']
                base_stat = stat_info['base_stat']
                self.stats[stat_name] = base_stat

        except Exception as e:
            print(f"Invalid ID.")
            exit()

    def display_info(self):
        print(f"Name: {self.name.capitalize()}")
        print(self.number)
        capitalize_types = [type.capitalize() for type in self.types]
        print(f"Type(s): {', '.join(capitalize_types)}")
        print()
        for i, ability in enumerate(self.abilities, start=1):
            if ability:
                print(f"Ability {i}: {ability.capitalize()}")
            else:
                pass
        print()
        print("Stats:")
        for stat_name, base_stat in self.stats.items():
            formatted_stat_name = ' '.join(word.capitalize() for word in stat_name.split('-'))
            print(f"  {formatted_stat_name}: {base_stat}")


# Example usage:
if __name__ == "__main__":
    pokemon_name = input("Enter Pokedex number or Pokemon name: ")
    print()
    pokemon = Pokemon(pokemon_name)
    pokemon.display_info()
