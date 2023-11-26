from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = 'cb5b0dee1898fc9d5889b79d431f63ec'
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    
    if not location:
        return jsonify({'error': 'Location not provided'}), 400
    
    params = {
        'q': location,
        'appid': API_KEY
    }

    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Not able to get weather data from openweather'}), 500

if __name__ == '__main__':
    app.run(debug=True)
