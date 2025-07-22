# visuals.py

import matplotlib.pyplot as plt

def calories_by_type(log):
    from collections import defaultdict

    totals = defaultdict(int)
    for act in log:
        totals[act["type"]] += act["calories"]

    types = list(totals.keys())
    calories = list(totals.values())

    plt.figure(figsize=(6, 4))
    plt.bar(types, calories, color="skyblue")
    plt.title("Calories Burned by Activity Type")
    plt.xlabel("Activity Type")
    plt.ylabel("Calories")
    plt.tight_layout()
    plt.show()
