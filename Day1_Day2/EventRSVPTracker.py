rsvp_list = {}

def add_guest():
    name = input("Enter guest name: ").strip().title()
    status = input("RSVP status (Yes/No/Maybe): ").strip().capitalize()
    if status not in ["Yes", "No", "Maybe"]:
        print("Invalid RSVP status. Please enter Yes, No, or Maybe.")
        return
    rsvp_list[name] = status
    print(f"{name} has been added with RSVP: {status}")

def view_guests():
    if not rsvp_list:
        print("No guests have RSVP'd yet.")
        return
    print("\nGuest List:")
    for name, status in rsvp_list.items():
        print(f"- {name}: {status}")

def update_rsvp():
    name = input("Enter guest name to update: ").strip().title()
    if name in rsvp_list:
        status = input("New RSVP status (Yes/No/Maybe): ").strip().capitalize()
        if status in ["Yes", "No", "Maybe"]:
            rsvp_list[name] = status
            print(f"{name}'s RSVP updated to: {status}")
        else:
            print("Invalid status.")
    else:
        print(f"{name} not found in the RSVP list.")

def remove_guest():
    name = input("Enter guest name to remove: ").strip().title()
    if name in rsvp_list:
        del rsvp_list[name]
        print(f"{name} removed from RSVP list.")
    else:
        print(f"{name} not found.")

def main():
    while True:
        print("\nEvent RSVP Tracker")
        print("1. Add Guest RSVP")
        print("2. View Guest List")
        print("3. Update RSVP")
        print("4. Remove Guest")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_guest()
        elif choice == '2':
            view_guests()
        elif choice == '3':
            update_rsvp()
        elif choice == '4':
            remove_guest()
        elif choice == '5':
            print("Exiting RSVP Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
