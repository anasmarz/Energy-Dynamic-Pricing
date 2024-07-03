from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model
with open('energy_pricing_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()
    features = [data['current_supply'], data['current_demand'], data['hour'], data['day_of_week'], data['historical_price']]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
