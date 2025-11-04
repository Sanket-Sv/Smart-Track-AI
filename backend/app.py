from flask import Flask, jsonify, request
from flask_cors import CORS
import joblib
import json
import pandas as pd
from utils.gps_handler import get_bus_location
from utils.eta_predictor import predict_eta
from utils.demand_forecaster import forecast_demand
from utils.delay_checker import check_delay
from utils.route_optimizer import optimize_route

app = Flask(__name__)
CORS(app)

# Load Models
eta_model = joblib.load("models/eta_model.pkl")
demand_model = joblib.load("models/demand_model.pkl")
delay_model = joblib.load("models/delay_detector.pkl")

# Routes Data
with open("routes/bus_routes.json") as f:
    routes = json.load(f)
with open("routes/stops.json") as f:
    stops = json.load(f)


@app.route('/')
def home():
    return jsonify({"message": "SmartTrack AI Backend Running"})


@app.route('/api/location/<bus_id>', methods=['GET'])
def bus_location(bus_id):
    """Get live GPS coordinates of a bus"""
    location = get_bus_location(bus_id)
    return jsonify(location)


@app.route('/api/eta', methods=['POST'])
def eta():
    """Predict ETA using trained ML model"""
    data = request.get_json()
    bus_id = data['bus_id']
    source = data['source']
    destination = data['destination']
    eta = predict_eta(eta_model, bus_id, source, destination)
    return jsonify({"bus_id": bus_id, "eta_minutes": eta})


@app.route('/api/demand_forecast', methods=['GET'])
def demand_forecast():
    """Predict future passenger demand"""
    forecast = forecast_demand(demand_model)
    return jsonify(forecast)


@app.route('/api/delay_status', methods=['POST'])
def delay_status():
    """Detect delay possibility"""
    data = request.get_json()
    delay_info = check_delay(delay_model, data)
    return jsonify(delay_info)


@app.route('/api/optimize_route', methods=['POST'])
def optimize():
    """Optimize route considering traffic & demand"""
    data = request.get_json()
    optimized = optimize_route(data)
    return jsonify(optimized)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
