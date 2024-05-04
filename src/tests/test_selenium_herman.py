from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open application (local IP address)
driver.get("http://127.0.0.1:5000")

# Test if the title of the webpage is correct
assert "Pokémon Info" in driver.title


"""
Test Case 1: Test Pikachu Data
"""
# Find the input box
input_box = driver.find_element(By.ID, "pokemon_number")

# Enter Pikachu in input box
input_box.send_keys("Pikachu")

# Submit the form (this clicks Enter on keyboard)
input_box.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(2)

# Check if the Pokemon image is displayed
pokemon_image = driver.find_element(By.CLASS_NAME, "pokemon_image")
assert pokemon_image.is_displayed()

# Check if Pikachu's image is displayed
expected_image_src = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
assert pokemon_image.get_attribute("src") == expected_image_src

# Check if the Pikachu's name and number is dispalyed correctly
pokemon_name = driver.find_element(By.CLASS_NAME, "pokemon_name")
expected_name_num_display = "Pikachu - #25"
assert pokemon_name.text == expected_name_num_display, f'Expected: {expected_name_num_display}, Got: {pokemon_name.text}'

# Check if the Types section is displayed
types_section = driver.find_element(By.CLASS_NAME, "type_container")
assert types_section.is_displayed()

# Check if the "Electric" is displayed
type_name = driver.find_element(By.CLASS_NAME, "type_name")
expected_type_name = "Electric"
assert type_name.text == expected_type_name, f'Expected: {expected_type_name}, Got: {type_name.text}'

# Check if "Static" and "Lightning Rod" are displayed as abilities
ability_section = driver.find_element(By.CLASS_NAME, "abilities_list")
assert ability_section.is_displayed()

ability_elements = ability_section.find_elements(By.CLASS_NAME, "ability")
abilities = [ability_element.text for ability_element in ability_elements]

assert "Static" in abilities, 'Expected Static, but could not find.'
assert "Lightning Rod" in abilities, 'Expected Lightning Rod, but could not find.'

# Check if all six stats are displayed correctly
stats_section = driver.find_element(By.CLASS_NAME, "stats_container")
assert stats_section.is_displayed()

stat_elements = stats_section.find_elements(By.CLASS_NAME, "stat_row")
stats = {}
for stat_element in stat_elements:
    stat_label = stat_element.find_element(By.CLASS_NAME, "stat_label").text
    stat_value = stat_element.find_element(By.CLASS_NAME, "stat_value").text
    stats[stat_label] = stat_value

# Check if all six stats are present and have values
expected_stats = {
    "HP:": "35",
    "Atk:": "55",
    "Def:": "40",
    "SpAtk:": "50",
    "SpDef:": "50",
    "Spd:": "90"
}

for stat_label, stat_value in expected_stats.items():
    assert stat_label in stats, f'Missing stat: {stat_label}'
    assert stats[stat_label] == stat_value, f'Expected {stat_label}: {stat_value}, Got: {stats[stat_label]}'


"""
Test Case 2: Test Iron Bundle data
"""
# Find the input box
input_box = driver.find_element(By.ID, "pokemon_number")

# Enter Pikachu in input box
input_box.send_keys("Iron Bundle")

# Submit the form (this clicks Enter on keyboard)
input_box.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(2)

# Check if the Pokemon image is displayed
pokemon_image = driver.find_element(By.CLASS_NAME, "pokemon_image")
assert pokemon_image.is_displayed()

# Check if Pikachu's image is displayed
expected_image_src = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/991.png"
assert pokemon_image.get_attribute("src") == expected_image_src

# Check if the Pikachu's name and number is dispalyed correctly
pokemon_name = driver.find_element(By.CLASS_NAME, "pokemon_name")
expected_name_num_display = "Iron Bundle - #991"
assert pokemon_name.text == expected_name_num_display, f'Expected: {expected_name_num_display}, Got: {pokemon_name.text}'

# Check if the Types section is displayed
types_section = driver.find_element(By.CLASS_NAME, "type_container")
assert types_section.is_displayed()

# Check if the "Electric" is displayed
type_names = driver.find_elements(By.CLASS_NAME, "type_name")
types = [type_name.text for type_name in type_names]

assert "Water" in types, 'Expected Water, but could not find.'
assert "Ice" in types, 'Expected Ice, but could not find.'

# Check if "Quark Drive" is the ability
ability_section = driver.find_element(By.CLASS_NAME, "abilities_list")
assert ability_section.is_displayed()

ability_elements = ability_section.find_elements(By.CLASS_NAME, "ability")
abilities = [ability_element.text for ability_element in ability_elements]

assert "Quark Drive" in abilities, 'Expected Static, but could not find.'

# Check if all six stats are displayed correctly
stats_section = driver.find_element(By.CLASS_NAME, "stats_container")
assert stats_section.is_displayed()

stat_elements = stats_section.find_elements(By.CLASS_NAME, "stat_row")
stats = {}
for stat_element in stat_elements:
    stat_label = stat_element.find_element(By.CLASS_NAME, "stat_label").text
    stat_value = stat_element.find_element(By.CLASS_NAME, "stat_value").text
    stats[stat_label] = stat_value

# Check if all six stats are present and have values
expected_stats = {
    "HP:": "56",
    "Atk:": "80",
    "Def:": "114",
    "SpAtk:": "124",
    "SpDef:": "60",
    "Spd:": "136"
}

for stat_label, stat_value in expected_stats.items():
    assert stat_label in stats, f'Missing stat: {stat_label}'
    assert stats[stat_label] == stat_value, f'Expected {stat_label}: {stat_value}, Got: {stats[stat_label]}'


"""
Test Case 3: Test Dropdown
"""
# Find the team dropdown box
team_dropdown = driver.find_element(By.ID, "team_dropdown")
team_dropdown.click()

# Find the 'sherman' selection
sherman_option = driver.find_element(By.XPATH, "//option[text()='sherman']")
sherman_option.click()

# Wait
time.sleep(2)

# Ensure that clicking the box takes you to edit/1
current_url = driver.current_url
expected_url = 'http://127.0.0.1:5000/edit/1'
assert current_url == expected_url, f'Expected: {expected_url}, Got: {current_url}'

"""
Test Case 4: Test Our Teams Button
"""
# Go back to the home page via the "Home" text in the header
home_nav_link = driver.find_element(By.CLASS_NAME, "nav_link")
home_nav_link.click()

# Find the 'Our Teams' button
teamlist_button_link = driver.find_element(By.ID, "teamlist_button")
teamlist_button_link.click()

# Wait
time.sleep(2)

# Ensure that clicking the box takes you to '/teamlist'
current_url = driver.current_url
expected_url = 'http://127.0.0.1:5000/teamlist'
assert current_url == expected_url, f'Expected: {expected_url}, Got: {current_url}'

"""
Test Case 5: Test Form Submission

We will edit sherman's first 3 Pokemon and test that they were updated correctly
"""

# Locate all edit buttons on the screen.
edit_buttons = driver.find_elements(By.CLASS_NAME, "edit_link")

# Since there are seven team members, and we want to find sherman's
# team, we will refer to the first edit button found.
edit_buttons[0].click()

# Wait
time.sleep(2)

# Ensure that clicking the box takes you to '/edit/1'
current_url = driver.current_url
expected_url = 'http://127.0.0.1:5000/edit/1'
assert current_url == expected_url, f'Expected: {expected_url}, Got: {current_url}'

# Find and locate input box 1, replace with Grimmsnarl.
input_box1 = driver.find_element(By.ID, "pokemon_name_1")
input_box1.click()
input_box1.clear() # Clear existing text
input_box1.send_keys("Grimmsnarl")

# Find and locate input box 2, replace with Hawlucha.
input_box2 = driver.find_element(By.ID, "pokemon_name_2")
input_box2.click()
input_box2.clear() # Clear existing text
input_box2.send_keys("Hawlucha")

# Find and locate input box 3, replace with Flutter Mane.
input_box3 = driver.find_element(By.ID, "pokemon_name_3")
input_box3.click()
input_box3.clear() # Clear existing text
input_box3.send_keys("Flutter Mane")

# Click enter to submit the form
input_box3.send_keys(Keys.RETURN)

# Go back to edit sherman's team
edit_buttons = driver.find_elements(By.CLASS_NAME, "edit_link")
edit_buttons[0].click()

# Wait
time.sleep(2)

# Get three edited values now:
edited_input_box1 = driver.find_element(By.ID, "pokemon_name_1")
edited_input_box2 = driver.find_element(By.ID, "pokemon_name_2")
edited_input_box3 = driver.find_element(By.ID, "pokemon_name_3")

# Get values in those inputu boxes
edited_value1 = edited_input_box1.get_attribute("value")
edited_value2 = edited_input_box2.get_attribute("value")
edited_value3 = edited_input_box3.get_attribute("value")

# Check for expected values
expected_value1 = "Grimmsnarl"
expected_value2 = "Hawlucha"
expected_value3 = "Flutter Mane"

# Assert the values
assert edited_value1 == expected_value1, f'Expected: {expected_value1}, Got {edited_value1}'
assert edited_value2 == expected_value2, f'Expected: {expected_value2}, Got {edited_value2}'
assert edited_value3 == expected_value3, f'Expected: {expected_value3}, Got {edited_value3}'

# Close the browser
driver.quit()