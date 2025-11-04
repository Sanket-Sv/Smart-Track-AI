def check_delay(model, data):
    """Use ML model to detect possible delay based on traffic & conditions"""
    bus_id = data.get("bus_id")
    traffic_level = data.get("traffic", 0.5)
    weather = data.get("weather", "clear")

    # Dummy rule for example
    delay_probability = 0.1 if weather == "clear" else 0.6
    return {"bus_id": bus_id, "delay_chance": round(delay_probability * 100, 2)}
