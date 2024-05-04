*** Settings ***
Library           SeleniumLibrary
Library           OperatingSystem

*** Variables ***
${BASE_URL}       http://localhost:5000

*** Test Cases ***
Test Index Page Header
    Open Browser    ${BASE_URL}    chrome    # Open index with Google Chrome.
    Page Should Contain    Enter Pokémon Name or Pokedex Number:    # Assert statement

Check Dropdown Options Count
    ${options_count}    Get Matching Xpath Count    //select[@id='team_dropdown']/option
    Should Be Equal As Integers    ${options_count}    7


Test 25 in Input Box
    Input Text  id=pokemon_number   25
    Click Button    xpath=//button[@type='submit']
    Location Should Be    http://localhost:5000/pokemon_details/25

Check for Pikachu
    Page Should Contain    Pikachu

Check for Electric
    Page Should Contain    Electric

Check for Static/Lightning Rod
    Page Should Contain    Static
    Page Should Contain    Lightning Rod
    Check Hover Text    Static   Paralyzes on contact.
    Check Hover Text    Lightning Rod    Draws electrical moves.

Check for Correct Stats
    ${hp_stat}    Get Text    xpath=//div[@class='stat_label'][contains(text(), 'HP')]/following-sibling::div[@class='stat_value']
    ${atk_stat}    Get Text    xpath=//div[@class='stat_label'][contains(text(), 'Atk')]/following-sibling::div[@class='stat_value']
    ${def_stat}    Get Text    xpath=//div[@class='stat_label'][contains(text(), 'Def')]/following-sibling::div[@class='stat_value']
    ${spatk_stat}    Get Text    xpath=//div[@class='stat_label'][contains(text(), 'SpAtk')]/following-sibling::div[@class='stat_value']
    ${spdef_stat}    Get Text    xpath=//div[@class='stat_label'][contains(text(), 'SpDef')]/following-sibling::div[@class='stat_value']
    ${spd_stat}    Get Text    xpath=//div[@class='stat_label'][contains(text(), 'Spd')]/following-sibling::div[@class='stat_value']
    Should Be Equal As Integers    ${hp_stat.strip()}    35
    Should Be Equal As Integers    ${atk_stat.strip()}    55
    Should Be Equal As Integers    ${def_stat.strip()}    40
    Should Be Equal As Integers    ${spatk_stat.strip()}    50
    Should Be Equal As Integers    ${spdef_stat.strip()}    50
    Should Be Equal As Integers    ${spd_stat.strip()}    90

Check Random Button
    Click Button    xpath=//button[@id='random_button']
    Location Should Contain    /pokemon_details/

Check for Stats Text
    Page Should Contain    Stats:
    
Check Our Teams Button
    Click Button    xpath=//button[@id='teamlist_button']
    Location Should Be    http://localhost:5000/teamlist

Check For All Members
    Page Should Contain    sherman
    Page Should Contain    bsiffer
    Page Should Contain    dkozlova
    Page Should Contain    dmiranda
    Page Should Contain    jasfoury
    Page Should Contain    aseay
    Page Should Contain    ajaramillo
    
Check First Edit Button
    Click Element    xpath=(//a[@class='edit_link'])[1]
    Location Should Be    http://localhost:5000/edit/1

Change First Pokemon To Pikachu
    Input Text  id=pokemon_name_1   pikachu
    Click Button    xpath=//button[@type='submit']

Confirm Page Redirection to Teamlist
    Location Should Be    http://localhost:5000/teamlist

Confirm Pikachu is First Pokemon
    ${first_pokemon_name}    Get Text    xpath=(//div[@class='member_container'])[1]//p[@class='pokemon_name']
    Should Be Equal    ${first_pokemon_name}    Pikachu

*** Keywords ***
Get Matching Xpath Count
    [Arguments]    ${xpath}
    ${elements}=    Get WebElements    xpath=${xpath}
    [Return]    ${elements.__len__() - 1}

Check Hover Text
    [Arguments]    ${ability_name}    ${expected_effect}
    Mouse Over    xpath=//p[@class='ability'][contains(text(), '${ability_name}')]
    Wait Until Element Is Visible    xpath=//p[@class='ability'][contains(text(), '${ability_name}')]/following-sibling::div[contains(@class, 'ability-effect-container')]
    ${actual_effect}=    Get Text    xpath=//p[@class='ability'][contains(text(), '${ability_name}')]/following-sibling::div[contains(@class, 'ability-effect-container')]
    Should Be Equal    ${actual_effect}    ${expected_effect}