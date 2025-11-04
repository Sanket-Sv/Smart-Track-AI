def optimize_route(data):
    """Return a recommended optimized route"""
    source = data.get("source")
    destination = data.get("destination")
    traffic = data.get("traffic", 0.4)

    if traffic > 0.7:
        route = f"Alternate route suggested for {source} → {destination}"
    else:
        route = f"Normal route for {source} → {destination}"

    return {"optimized_route": route, "traffic_level": traffic}
