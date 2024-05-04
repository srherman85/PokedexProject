from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# First we open the browser to the correct webpage

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")
time.sleep(3)

# Next we check to see if the title of our webpage is correct

pageTitle = driver.title
titleExpected = "Pokémon Info"
if pageTitle == titleExpected:
    print("The title is verified as expected.")
else:
    print("The title verification has FAILED!")
    driver.quit()
time.sleep(1)

# Next we will test to see if the input for a Pokemon name is working correctly

input_box = driver.find_element(By.ID, "pokemon_number")
input_box.send_keys("Squirtle")
time.sleep(1)
input_button = driver.find_element(By.ID, "submit_button")
input_button.click()
time.sleep(1)

# Now we will test the random button to see if it works
randomButton = driver.find_element(By.ID, "random_button")
randomButton.click()
time.sleep(3)

# Next up we will take a look at our teams

ourTeamsButton = driver.find_element(By.ID, "teamlist_button")
ourTeamsButton.click()
time.sleep(3)
driver.back()
time.sleep(3)