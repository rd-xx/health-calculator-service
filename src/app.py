from flask import Flask
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    if height is None or weight is None:
        return jsonify({"error": "Missing required parameters 'height' and 'weight'"}), 400
    
    bmi_value = calculate_bmi(height, weight)
    return jsonify({"bmi": bmi_value})

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    gender = data.get('gender')
    
    if None in (height, weight, age, gender):
        return jsonify({"error": "Missing required parameters 'height', 'weight', 'age', and 'gender'"}), 400
    
    bmr_value = calculate_bmr(height, weight, age, gender)
    return jsonify({"bmr": bmr_value})

if __name__ == "__main__":
    app.run(debug=True)
    print("hello")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)