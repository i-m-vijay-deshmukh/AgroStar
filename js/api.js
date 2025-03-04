async function fetchLiveData() {
    try {
        console.log("Fetching live agricultural data...");

        const response = await fetch("http://localhost:5000/data");

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
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
            <p style="color: red;">⚠️ Failed to load live updates. Please try again later.</p>
        `;
    }
}

// Load data when page loads
document.addEventListener("DOMContentLoaded", fetchLiveData);
