import random
import pandas as pd
from src.simulator import run_simulation

def generate_data(n=1000):
    data = []

    for _ in range(n):
        arrival_rate = random.uniform(1, 10)   # lower=1, upper=10
        service_time = random.uniform(1, 8)    # lower=1, upper=8
        capacity = random.randint(1, 5)        # lower=1, upper=5

        avg_wait = run_simulation(arrival_rate, service_time, capacity)
        data.append([arrival_rate, service_time, capacity, avg_wait])

    df = pd.DataFrame(data, columns=[
        "ArrivalRate", "ServiceTime", "Capacity", "AvgWaitingTime"
    ])

    df.to_csv("data/simulation_data.csv", index=False)
    return df
