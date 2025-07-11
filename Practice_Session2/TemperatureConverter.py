# Input: Temperature in Celsius
celsius_input = input("Enter temperature in Celsius: ")

# Validate input
if celsius_input.replace('.', '', 1).isdigit():
    celsius = float(celsius_input)

    # Convert to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Categorize temperature
    if celsius < 20:
        category = "Cold"
    elif 20 <= celsius <= 30:
        category = "Warm"
    else:
        category = "Hot"

    # Display output
    print(f"Temperature: {celsius}°C / {fahrenheit:.1f}°F → {category}")
else:
    print("Invalid input. Please enter a valid number.")
