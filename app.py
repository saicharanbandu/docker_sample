from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    inputs = np.array(data['inputs']).reshape(1, -1)
    prediction = model.predict(inputs).tolist()
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)