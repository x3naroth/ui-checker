from flask import Flask, request, jsonify
from keras.models import load_model

app = Flask(__name__)

# Cargar el modelo h5
model = load_model('modelo.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Realiza una predicción con los datos de entrada
        prediction = model.predict(data)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
