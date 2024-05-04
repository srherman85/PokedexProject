document.addEventListener('DOMContentLoaded', function() {
    const pokemonNameInputs = document.querySelectorAll('input[type="text"]');
    const form = document.querySelector('form');
    const submitButton = document.querySelector('button[type="submit"]');

    pokemonNameInputs.forEach(function(input) {
        input.addEventListener('input', async function(event) {
            const inputId = event.target.id;
            const index = inputId.split('_')[2];

            const newName = event.target.value.trim();
            if (newName !== '') {
                try {
                    const formData = new FormData();
                    formData.append('pokemon_name', newName);

                    const response = await fetch('/get_pokemon_number', {
                        method: 'POST',
                        body: formData
                    });

                    if (response.ok) {
                        const pokemonNumber = await response.json();
                        if (pokemonNumber) {
                            const numberInput = document.getElementById(`pokemon_number_${index}`);
                            const pokemonImage = document.querySelector(`img.pokemon_in_form_image:nth-of-type(${index})`);
                            numberInput.value = pokemonNumber;
                            pokemonImage.src = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${pokemonNumber}.png`;
                            pokemonImage.alt = newName;
                            // Re-enable the submit button
                            submitButton.disabled = false;
                        } else {
                            // Clear the image and number fields if the Pokémon number is not found
                            const numberInput = document.getElementById(`pokemon_number_${index}`);
                            const pokemonImage = document.querySelector(`img.pokemon_in_form_image:nth-of-type(${index})`);
                            numberInput.value = '';
                            pokemonImage.src = '';
                            pokemonImage.alt = '';
                            // Disable the submit button
                            submitButton.disabled = true;
                            // Display error message
                            displayErrorMessage('Pokemon not found!');
                        }
                    } else {
                        console.error('Failed to get Pokémon number');
                    }
                } catch (error) {
                    console.error('Error:', error);
                }
            } else {
                // Clear the image and number fields if the Pokémon name is empty
                const numberInput = document.getElementById(`pokemon_number_${index}`);
                const pokemonImage = document.querySelector(`img.pokemon_in_form_image:nth-of-type(${index})`);
                numberInput.value = '';
                pokemonImage.src = '';
                pokemonImage.alt = '';
                // Disable the submit button
                submitButton.disabled = true;
            }
        });
    });

    function displayErrorMessage(message) {
        const errorMessage = document.createElement('div');
        errorMessage.classList.add('error-message');
        errorMessage.textContent = message;
        form.appendChild(errorMessage);
    }

    form.addEventListener('submit', function(event) {
        if (submitButton.disabled) {
            event.preventDefault();
            displayErrorMessage('Please enter a valid Pokémon name.');
        }
    });
});
