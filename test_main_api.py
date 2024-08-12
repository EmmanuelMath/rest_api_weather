from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# check if the main API is working correctly
@app.route('/test-weather-api', methods=['GET'])
def test_weather_api():
    # Extract city and date from the query parameters
    city = request.args.get('city')
    date = request.args.get('date')
    
    if not city or not date:
        return jsonify({"error": "City and date parameters are required"}), 400
    
    main_api_url = f"http://127.0.0.1:5000/city/city={city}&date={date}"
    
    try:
        # Send a GET request to the main API
        response = requests.get(main_api_url)
        response_data = response.json()
        
        # Check if the main API returned an error
        if "error" in response_data:
            return jsonify({"error": "Main API returned an error", "details": response_data}), 500
        
        # Return the data received from the main API
        return jsonify({
            "message": "Main API is working correctly",
            "data": response_data
        })
    
    except Exception as exc:
        # Handle any exceptions that occur during the request
        return jsonify({"error": str(exc)}), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)
