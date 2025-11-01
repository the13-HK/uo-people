document.getElementById('convertButton').addEventListener('click', function() {
    const temperatureInput = document.getElementById('temperatureInput').value;
    const unitSelect = document.getElementById('unitSelect').value;
    const resultText = document.getElementById('resultText');

    // Clear previous result
    resultText.textContent = '';

    // Validate input
    if (isNaN(temperatureInput) || temperatureInput === '') {
        resultText.textContent = 'Please enter a valid numeric temperature.';
        resultText.style.color = 'red';
        return;
    }

    const temperature = parseFloat(temperatureInput);
    let convertedTemperature;

    // Perform conversion based on selected unit
    if (unitSelect === 'Celsius') {
        convertedTemperature = (temperature * 9/5) + 32; // Celsius to Fahrenheit
        resultText.textContent = `${temperature}°C is ${convertedTemperature.toFixed(2)}°F`;
    } else {
        convertedTemperature = (temperature - 32) * 5/9; // Fahrenheit to Celsius
        resultText.textContent = `${temperature}°F is ${convertedTemperature.toFixed(2)}°C`;
    }
    resultText.style.color = 'black';
});