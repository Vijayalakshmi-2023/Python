def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(c):.2f}")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"Temperature in Celsius: {fahrenheit_to_celsius(f):.2f}")
    elif choice == '3':
        c = float(input("Enter temperature in Celsius: "))
        print(f"Temperature in Kelvin: {celsius_to_kelvin(c):.2f}")
    elif choice == '4':
        k = float(input("Enter temperature in Kelvin: "))
        print(f"Temperature in Celsius: {kelvin_to_celsius(k):.2f}")
    elif choice == '5':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"Temperature in Kelvin: {fahrenheit_to_kelvin(f):.2f}")
    elif choice == '6':
        k = float(input("Enter temperature in Kelvin: "))
        print(f"Temperature in Fahrenheit: {kelvin_to_fahrenheit(k):.2f}")
    else:
        print("Invalid option. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
