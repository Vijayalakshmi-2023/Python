from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

age = calculate_age(birth_date)
print(f"You are {age} years old.")
