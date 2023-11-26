from flask import Flask, request, jsonify
import requests

app = Flask(name)

OPENWEATHERMAP_API_KEY = "fb428e0d4638d5489ed8a473069aa0a2"
OPENWEATHERMAP_API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

@app.route('/weather/<location>', methods=['GET'])
def get_weather(location):
    api_url = OPENWEATHERMAP_API_URL.format(location, OPENWEATHERMAP_API_KEY)
    response = requests.get(api_url)
    
    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Unable to fetch weather data"}), 500

if name == 'main':
    app.run(debug=True)
