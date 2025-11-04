import random

def get_bus_location(bus_id):
    """Simulate real-time GPS location for a bus"""
    # In production: integrate actual GPS API or database feed
    lat = round(28.6 + random.uniform(-0.01, 0.01), 6)
    lon = round(77.2 + random.uniform(-0.01, 0.01), 6)
    return {"bus_id": bus_id, "latitude": lat, "longitude": lon}
