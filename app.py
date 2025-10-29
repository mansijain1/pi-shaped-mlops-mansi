from flask import Flask, request, jsonify
import joblib
import numpy as np
import traceback

app = Flask(__name__)

model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Iris Prediction API!",
        "endpoints": {
            "GET /health": "Check API health",
            "POST /predict": "Make a prediction"
        }
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = data.get("features", None)
        if features is None:
            return jsonify({"error": "Missing 'features' field"}), 400

        features = np.array(features).reshape(1, -1)
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)
        
        species = {0: "setosa", 1: "versicolor", 2: "virginica"}
        return jsonify({
            "prediction": species[int(prediction[0])]
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
