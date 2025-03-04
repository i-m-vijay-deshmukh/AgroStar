import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# 🔑 Replace with your API Key
WEATHER_API_KEY = "48258aedd23143debbe190309250303"  # Get from https://www.weatherapi.com/
MARKET_PRICE_URL = "https://agmarknet.gov.in/"  # AGMARKNET website for market prices

def scrape_market_prices():
    try:
        response = requests.get(MARKET_PRICE_URL)
        if response.status_code != 200:
            return {"error": "Failed to fetch market prices"}

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Modify this part based on AGMARKNET's structure
        market_prices = {}
        price_table = soup.find("table")  # Adjust based on actual HTML structure
        
        if price_table:
            rows = price_table.find_all("tr")
            for row in rows[1:]:  # Skipping the header row
                cols = row.find_all("td")
                if len(cols) >= 2:
                    commodity = cols[0].text.strip()
                    price = cols[1].text.strip()
                    market_prices[commodity] = price
        
        return market_prices if market_prices else {"error": "No price data found"}

    except Exception as e:
        return {"error": f"Scraping failed: {str(e)}"}

@app.route("/data", methods=["GET"])
def get_data():
    try:
        # 🌤 Fetch Weather Data
        weather_url = f"https://api.weatherapi.com/v1/current.json?key=48258aedd23143debbe190309250303&q=howrah"
        weather_response = requests.get(weather_url)

        if weather_response.status_code != 200:
            return jsonify({"error": "Failed to fetch weather data"}), 500  # Error handling

        weather_data = weather_response.json()

        # 🏛 Scrape Market Price Data
        market_price_data = scrape_market_prices()

        # 📊 Format Data
        data = {
            "weather": f"{weather_data['current']['condition']['text']}, {weather_data['current']['temp_c']}°C",
            "market_price": market_price_data,
            "soil_moisture": "Moderate",  # TODO: Add real IoT integration
            "advisory": "Irrigate fields early morning to reduce water loss."
        }

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": f"Failed to fetch live data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
