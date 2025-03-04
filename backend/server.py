import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# 🔑 Replace with your API Key
WEATHER_API_KEY = "48258aedd23143debbe190309250303"  # Get from https://www.weatherapi.com/
MARKET_PRICE_API_URL = "https://api.example.com/market_prices"  # Replace with real source

@app.route("/data", methods=["GET"])
def get_data():
    try:
        
        # 🌤 Fetch Weather Data
        weather_url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=Delhi"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        # 🏛 Fetch Market Price Data (Replace with a real API)
        market_price_response = requests.get(MARKET_PRICE_API_URL)
        market_price_data = market_price_response.json() if market_price_response.status_code == 200 else {}

        # 📊 Format Data
        data = {
            "weather": f"{weather_data['current']['condition']['text']}, {weather_data['current']['temp_c']}°C",
            "market_price": {
                "Wheat": market_price_data.get("Wheat", "Not Available"),
                "Rice": market_price_data.get("Rice", "Not Available")
            },
            "soil_moisture": "Moderate",  # TODO: Add real IoT integration
            "advisory": "Irrigate fields early morning to reduce water loss."
        }

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": f"Failed to fetch live data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
