document.addEventListener('DOMContentLoaded', function() {
    var inputField = document.getElementById('pokemon_number');
    var randomButton = document.getElementById('random_button');
    var form = document.querySelector('form');
    var errorMessage = document.getElementById('error_message');

    randomButton.addEventListener('click', function() {
        var randomNumber = Math.floor(Math.random() * 1026) + 1;
        inputField.value = randomNumber;
        form.submit();
    });

    form.addEventListener('submit', function(event) {
        var inputValue = inputField.value.trim();
        if (!isValidInput(inputValue)) {
            errorMessage.textContent = "Invalid input. Please enter a valid Pokémon name or Pokedex number.";
            event.preventDefault(); // Prevent form submission
        } else {
            // If input is a number, submit the form directly
            if (/^\d+$/.test(inputValue)) {
                return;
            }
            // If input is a name, format it and submit the form
            formatNameAndSubmit(inputValue);
        }
    });

    function isValidInput(input) {
        // Validate if input is a valid Pokémon name or number
        if (!input.match(/^[a-zA-Z\s]*$/) && !/^\d+$/.test(input)) {
            return false;
        }
        // If input is a number, check if it's within the valid range
        if (/^\d+$/.test(input) && (parseInt(input) < 1 || parseInt(input) > 1026)) {
            return false;
        }
        return true;
    }

    function formatNameAndSubmit(name) {
        // Format the name (replace spaces with hyphens)
        var formattedName = name.trim().toLowerCase().replace(/\s+/g, '-');
        inputField.value = formattedName;
        form.submit();
    }
});
