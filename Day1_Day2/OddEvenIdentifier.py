def odd_even():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    odd_even()
