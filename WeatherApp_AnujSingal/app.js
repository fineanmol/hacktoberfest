document.getElementById('search-btn').addEventListener('click', async function(event) {
    event.preventDefault(); 

    const city = document.getElementById('city').value;
    const apiKey = 'cf1dbf46dfabab8ffaab0c579bc73f13';
    const url = `https://api.weatherstack.com/current?access_key=${apiKey}&query=${city}`;
    
    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.success !== false) { 
            const weather = data.current.weather_descriptions[0]; 
            const temp = data.current.temperature; 
            const humidity = data.current.humidity;
            const windSpeed = data.current.wind_speed; 

            document.getElementById('weather-info').innerHTML =
                `<div><strong>Weather:</strong> ${weather}</div>
                <div><strong>Temperature:</strong> ${temp}°C</div>
                <div><strong>Humidity:</strong> ${humidity}%</div>
                <div><strong>Wind Speed:</strong> ${windSpeed} km/h</div>`;
            document.getElementById('error').style.display = 'none'; 
        } 
        else {
            document.getElementById('error').style.display = 'block';
            document.getElementById('error').textContent = 'City not found. Please try again.';
            document.getElementById('weather-info').innerHTML = ''; 
        }
    } catch (error) {
        console.error('Error fetching the weather data:', error);
        document.getElementById('error').style.display = 'block';
        document.getElementById('error').textContent = 'Something went wrong. Please try again later.';
    }
});

