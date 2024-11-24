from flask import Flask, request, jsonify
from flask_cors import CORS # type: ignore
import requests

app = Flask(__name__)
CORS(app) 


@app.route('/convert', methods=['GET'])
def convert_date():
    """
    Converts a Gregorian date to a Hebrew date using the Hebcal API.
    Takes 'year', 'month', and 'day' as query parameters from the URL.
    
    Returns:
        json: A JSON object containing the Hebrew date.
    """
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')

    url = f"https://www.hebcal.com/converter?cfg=json&gy={year}&gm={month}&gd={day}&g2h=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

    except ValueError as e:
        # Handle JSON decoding errors
        return jsonify({"error": "Error decoding JSON data from API", "details": str(e)}), 500
    
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
