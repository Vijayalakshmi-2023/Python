# Temperature Category Classifier

# Step 1: Input list of temperatures (example list)
temperatures = [15, 22, 30, 35, 18, 28]

# Step 2: Classify each temperature using for loop and conditions
print("----- Temperature Classification -----")
for temp in temperatures:
    if temp < 20:
        category = "Cold"
    elif 20 <= temp <= 30:
        category = "Warm"
    else:
        category = "Hot"
    
    print(f"{temp}°C → {category}")
print("--------------------------------------")
