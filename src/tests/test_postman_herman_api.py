"""
File: test_postman_herman_api.py
Shannon Herman
14 Mar 2024

This application tests the pokeapi API.

PokeAPI Main Site: https://pokeapi.co/https://pokeapi.co/

1. Pokemon Number to Name Validation
2. Pokemon Number to Attack Stat Validation
3. Pokemon Number to Defense Stat Validation
4. Pokemon Number to Sp. Atk Stat Validation
5. Pokemon Number to Sp. Def Stat Validation
6. Pokemon Number to Speed Stat Validation
7. Pokemon Number to Ability/Abilities Validation
"""

# If requests is not installed, open command line and issue
# this command: pip install requests
import requests

# If pytest is not installed, open command line and issue
# this command: pip install pytest
import pytest

# This is the base URL:
BASE_URL = "https://pokeapi.co/api/v2"


# 1. Number --> Name Validation
@pytest.mark.parametrize("pokemon_number, expected_name", [
    (1, "bulbasaur"),
    (232, "donphan"),
    (405, "luxray"),
    (770, "palossand"),
    (811, "thwackey"),
    (148, "dragonair"),
    (233, "porygon2"),
    (158, "totodile"),
    (61, "poliwhirl"),
    (987, "flutter-mane"),  # hyphenated
])

def test_pokeapi_get_pokemon_from_number(pokemon_number, expected_name):
    """
    Test to ensure Pokemon #s match Names
    """
    response = requests.get(f'{BASE_URL}/pokemon/{pokemon_number}')

    # Ensure that API Request was OK
    assert response.status_code == 200, f'Failed to fetch Pokemon at #{pokemon_number}'

    # Parse
    pokemon_data = response.json()

    # Assert
    assert pokemon_data["name"] == expected_name, f'Expected {expected_name} but got {pokemon_data["name"]}'


# 2. Number --> Attack Stat Validation
@pytest.mark.parametrize("pokemon_number, expected_atk_stat", [
    (27, 75),
    (119, 92),
    (247, 84),
    (309, 45),
    (428, 76),
    (542, 103),
    (645, 125),
    (720, 110),
    (806, 127),
    (952, 108),
])
def test_pokeapi_get_atk_stat_from_number(pokemon_number, expected_atk_stat):
    """
    Test to ensure Pokemon #s match Attack Stats
    """
    response = requests.get(f'{BASE_URL}/pokemon/{pokemon_number}')

    # Ensure that API Request was OK
    assert response.status_code == 200, f'Failed to fetch Pokemon at #{pokemon_number}'

    # Parse
    pokemon_data = response.json()

    # Assert
    assert pokemon_data["stats"][1][
               "base_stat"] == expected_atk_stat, f'Expected {expected_atk_stat} but got {pokemon_data["stats"][1]["base_stat"]}'


# 3. Number --> Defense Stat Validation
@pytest.mark.parametrize("pokemon_number, expected_def_stat", [
    (37, 40),
    (135, 60),
    (216, 50),
    (322, 40),
    (441, 45),
    (553, 80),
    (658, 67),
    (712, 85),
    (861, 65),
    (924, 45),
])
def test_pokeapi_get_def_stat_from_number(pokemon_number, expected_def_stat):
    """
    Test to ensure Pokemon #s match Defense Stats
    """
    response = requests.get(f'{BASE_URL}/pokemon/{pokemon_number}')

    # Ensure that API Request was OK
    assert response.status_code == 200, f'Failed to fetch Pokemon at #{pokemon_number}'

    # Parse
    pokemon_data = response.json()

    # Assert
    assert pokemon_data["stats"][2][
               "base_stat"] == expected_def_stat, f'Expected {expected_def_stat} but got {pokemon_data["stats"][2]["base_stat"]}'


# 4. Number --> Special Attack Stat Validation
@pytest.mark.parametrize("pokemon_number, expected_spatk_stat", [
    (12, 90),
    (159, 59),
    (272, 90),
    (378, 100),
    (464, 55),
    (573, 65),
    (672, 62),
    (754, 80),
    (884, 120),
    (964, 53),
])
def test_pokeapi_get_spatk_stat_from_number(pokemon_number, expected_spatk_stat):
    """
    Test to ensure Pokemon #s match Special Attack Stats
    """
    response = requests.get(f'{BASE_URL}/pokemon/{pokemon_number}')

    # Ensure that API Request was OK
    assert response.status_code == 200, f'Failed to fetch Pokemon at #{pokemon_number}'

    # Parse
    pokemon_data = response.json()

    # Assert
    assert pokemon_data["stats"][3][
               "base_stat"] == expected_spatk_stat, f'Expected {expected_spatk_stat} but got {pokemon_data["stats"][3]["base_stat"]}'


# 5. Number --> Special Defense Stat Validation
@pytest.mark.parametrize("pokemon_number, expected_spdef_stat", [
    (98, 25),
    (150, 90),
    (234, 65),
    (356, 130),
    (481, 105),
    (567, 65),
    (645, 80),
    (763, 98),
    (848, 35),
    (956, 60),
])
def test_pokeapi_get_spdef_stat_from_number(pokemon_number, expected_spdef_stat):
    """
    Test to ensure Pokemon #s match Special Defense Stats
    """
    response = requests.get(f'{BASE_URL}/pokemon/{pokemon_number}')

    # Ensure that API Request was OK
    assert response.status_code == 200, f'Failed to fetch Pokemon at #{pokemon_number}'

    # Parse
    pokemon_data = response.json()

    # Assert
    assert pokemon_data["stats"][4][
               "base_stat"] == expected_spdef_stat, f'Expected {expected_spdef_stat} but got {pokemon_data["stats"][4]["base_stat"]}'


# 6. Number --> Speed Stat Validation
@pytest.mark.parametrize("pokemon_number, expected_speed_stat", [
    (65, 120),
    (190, 85),
    (260, 60),
    (343, 55),
    (441, 91),
    (556, 60),
    (670, 52),
    (768, 40),
    (853, 42),
    (954, 45),
])
def test_pokeapi_get_speed_stat_from_number(pokemon_number, expected_speed_stat):
    """
    Test to ensure Pokemon #s match Speed Stats
    """
    response = requests.get(f'{BASE_URL}/pokemon/{pokemon_number}')

    # Ensure that API Request was OK
    assert response.status_code == 200, f'Failed to fetch Pokemon at #{pokemon_number}'

    # Parse
    pokemon_data = response.json()

    # Assert
    assert pokemon_data["stats"][5][
               "base_stat"] == expected_speed_stat, f'Expected {expected_speed_stat} but got {pokemon_data["stats"][5]["base_stat"]}'

# 7. Number --> Ability Validation
@pytest.mark.parametrize("pokemon_number, expected_abilities", [
    (29, ['poison-point', 'rivalry', 'hustle']),
    (121, ['illuminate', 'natural-cure', 'analytic']),
    (223, ['hustle', 'sniper', 'moody']),
    (335, ['immunity', 'toxic-boost']),
    (442, ['pressure', 'infiltrator']),
    (526, ['sturdy', 'sand-stream', 'sand-force']),
    (616, ['hydration', 'shell-armor', 'overcoat']),
    (722, ['overgrow', 'long-reach']),
    (800, ['prism-armor']),
    (934, ['purifying-salt', 'sturdy', 'clear-body']),
])
def test_pokeapi_get_abilities_from_number(pokemon_number, expected_abilities):
    """
    Test to ensure Pokemon #s match Abilities
    """
    response = requests.get(f'{BASE_URL}/pokemon/{pokemon_number}')

    # Ensure that API Request was OK
    assert response.status_code == 200, f'Failed to fetch Pokemon at #{pokemon_number}'

    # Parse
    pokemon_data = response.json()

    # Get Abilities
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]

    # Assert
    assert set(abilities) == set(expected_abilities), f'Expected {expected_abilities}, but got {abilities}'
