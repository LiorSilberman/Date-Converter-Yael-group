from flask import Flask, request, jsonify
from flask_cors import CORS
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

    response = requests.get(url)
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
