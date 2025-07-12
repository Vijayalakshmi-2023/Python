# Travel Bucket List
bucket_list = []

def show_menu():
    print("\n🌍 Travel Bucket List")
    print("1. View all places")
    print("2. Add a place")
    print("3. Remove a place")
    print("4. Update a place")
    print("5. Check if a place is on the list")
    print("6. Exit")

def view_places():
    if not bucket_list:
        print("Your bucket list is empty.")
    else:
        print("\n🗺️ Places You Want to Visit:")
        for idx, place in enumerate(bucket_list, 1):
            print(f"{idx}. {place}")

def add_place():
    place = input("Enter a place to add: ").strip().title()
    if place in bucket_list:
        print(f"⚠️ '{place}' is already on your list.")
    else:
        bucket_list.append(place)
        print(f"✅ '{place}' added to your bucket list.")

def remove_place():
    place = input("Enter the place to remove: ").strip().title()
    if place in bucket_list:
        bucket_list.remove(place)
        print(f"🗑️ '{place}' removed from your list.")
    else:
        print(f"❌ '{place}' is not on your list.")

def update_place():
    old_place = input("Enter the place to update: ").strip().title()
    if old_place in bucket_list:
        new_place = input("Enter the new name for the place: ").strip().title()
        index = bucket_list.index(old_place)
        bucket_list[index] = new_place
        print(f"🔄 Updated '{old_place}' to '{new_place}'.")
    else:
        print(f"❌ '{old_place}' not found on the list.")

def check_place():
    place = input("Enter the place to check: ").strip().title()
    if place in bucket_list:
        print(f"✅ Yes! '{place}' is on your bucket list.")
    else:
        print(f"❌ '{place}' is not on your list yet.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1–6): ")

    if choice == "1":
        view_places()
    elif choice == "2":
        add_place()
    elif choice == "3":
        remove_place()
    elif choice == "4":
        update_place()
    elif choice == "5":
        check_place()
    elif choice == "6":
        print("Goodbye! May all your travel dreams come true. ✈️🌟")
        break
    else:
        print("Invalid option. Please try again.")
