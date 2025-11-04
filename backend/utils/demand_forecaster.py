import pandas as pd
import random

def forecast_demand(model):
    """Return passenger demand forecast for the next 6 hours"""
    # Simulated data
    hours = list(range(1, 7))
    demand = [int(random.uniform(30, 120)) for _ in hours]
    return {"hours_ahead": hours, "predicted_demand": demand}
