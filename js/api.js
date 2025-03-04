async function fetchLiveData() {
    try {
        console.log("Fetching live agricultural data...");

        const response = await fetch("https://your-flask-api.onrender.com/data");

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error(`Resource not found: ${response.url}`);
            } else {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
        }

        // Validate response format
        let data;
        try {
            data = await response.json();
        } catch (e) {
            throw new Error("Response cannot be parsed as JSON");
        }

        console.log("Received Data:", data);

        // Update UI with Live Data
        document.getElementById("live-data").innerHTML = `
            <h3>🌤 Weather: ${data.weather}</h3>
            <h3>💰 Market Prices:</h3>
            <ul>
                <li>🌾 Wheat: ${data.market_price.Wheat}</li>
                <li>🍚 Rice: ${data.market_price.Rice}</li>
            </ul>
            <h3>🌱 Soil Moisture: ${data.soil_moisture}</h3>
            <h3>📢 Advisory: ${data.advisory}</h3>
        `;

    } catch (error) {
        console.error("Error fetching data:", error);
        document.getElementById("live-data").innerHTML = `
            <p style="color: red;">⚠️ Failed to load live updates. ${error.message}. Please try again later.</p>
        `;
    }
}

// Call the function to fetch live data
fetchLiveData();
