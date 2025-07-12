# Event Guest List Manager

guest_list = []

def show_menu():
    print("\n📋 Event Guest List Menu")
    print("1. View guest list")
    print("2. Add a guest")
    print("3. Remove a guest")
    print("4. Check if someone is invited")
    print("5. Show total number of guests")
    print("6. Exit")

def view_guests():
    if not guest_list:
        print("📭 The guest list is currently empty.")
    else:
        print("\n🎉 Current Guests:")
        for guest in guest_list:
            print(f"- {guest}")

def add_guest():
    name = input("Enter guest name to add: ").strip().title()
    if name in guest_list:
        print(f"⚠️ {name} is already on the guest list.")
    else:
        guest_list.append(name)
        print(f"✅ {name} added to the guest list.")

def remove_guest():
    name = input("Enter guest name to remove: ").strip().title()
    if name in guest_list:
        guest_list.remove(name)
        print(f"🗑️ {name} has been removed from the guest list.")
    else:
        print(f"❌ {name} was not found in the guest list.")

def check_guest():
    name = input("Enter guest name to check: ").strip().title()
    if name in guest_list:
        print(f"✅ {name} is invited to the event.")
    else:
        print(f"❌ {name} is not on the guest list.")

def total_guests():
    print(f"👥 Total guests invited: {len(guest_list)}")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1–6): ")

    if choice == "1":
        view_guests()
    elif choice == "2":
        add_guest()
    elif choice == "3":
        remove_guest()
    elif choice == "4":
        check_guest()
    elif choice == "5":
        total_guests()
    elif choice == "6":
        print("Goodbye! 🥳 Event planning complete.")
        break
    else:
        print("❌ Invalid option. Please try again.")
