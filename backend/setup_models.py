import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

# === ETA MODEL (predicts travel time) ===
eta_model = LinearRegression()
X_eta = np.array([[1], [2], [3], [4], [5]])
y_eta = np.array([10, 20, 30, 40, 50])
eta_model.fit(X_eta, y_eta)
joblib.dump(eta_model, "models/eta_model.pkl")

# === DEMAND MODEL (predicts passenger demand) ===
demand_model = LinearRegression()
X_demand = np.array([[10], [20], [30], [40], [50]])
y_demand = np.array([100, 200, 300, 400, 500])
demand_model.fit(X_demand, y_demand)
joblib.dump(demand_model, "models/demand_model.pkl")

# === DELAY DETECTOR (simple classifier) ===
from sklearn.linear_model import LogisticRegression
delay_detector = LogisticRegression()
X_delay = np.array([[5], [10], [15], [20], [25]])
y_delay = np.array([0, 0, 1, 1, 1])  # 1 = delayed
delay_detector.fit(X_delay, y_delay)
joblib.dump(delay_detector, "models/delay_detector.pkl")

print("✅ Dummy models created successfully inside 'backend/models/'!")
