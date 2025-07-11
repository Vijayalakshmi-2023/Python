def explore_data_type():
    user_input = input("Enter anything: ")

    try:
        val_int = int(user_input)
        print(f"Interpreted as Integer: {val_int}")
    except ValueError:
        print("Not an Integer.")

    try:
        val_float = float(user_input)
        print(f"Interpreted as Float: {val_float}")
    except ValueError:
        print("Not a Float.")

    if user_input.lower() in ['true', 'false']:
        val_bool = user_input.lower() == 'true'
        print(f"Interpreted as Boolean: {val_bool}")
    else:
        print("Not a Boolean.")

    print(f"Always interpreted as String: '{user_input}'")

if __name__ == "__main__":
    explore_data_type()
