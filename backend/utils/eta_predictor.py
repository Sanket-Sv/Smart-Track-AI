import pandas as pd

def predict_eta(model, bus_id, source, destination):
    """Predict ETA in minutes using trained ML model"""
    # Dummy input features (real version would use GPS distance, traffic, etc.)
    features = pd.DataFrame([[bus_id, len(source), len(destination)]],
                            columns=['bus_id', 'src_len', 'dest_len'])
    prediction = model.predict(features)[0]
    return round(prediction, 2)
