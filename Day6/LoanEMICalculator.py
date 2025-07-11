def calculate_emi(principal, rate, time_years):
    # Convert annual rate to monthly and time to months
    r = rate / (12 * 100)         # monthly interest rate
    n = time_years * 12           # total number of months

    # EMI formula:
    # EMI = [P × r × (1 + r)^n] / [(1 + r)^n – 1]
    emi_formula = lambda p, r, n: (p * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)

    # Handle zero interest gracefully
    if rate == 0:
        return round(principal / n, 2)
    
    emi = emi_formula(principal, r, n)
    return round(emi, 2)

try:
    p = float(input("Enter loan amount (principal): "))
    r = float(input("Enter annual interest rate (%): "))
    t = int(input("Enter loan duration in years: "))

    monthly_emi = calculate_emi(p, r, t)
    print(f"\n💰 Monthly EMI: ₹{monthly_emi}")

except ValueError:
    print("❌ Please enter valid numerical input.")
