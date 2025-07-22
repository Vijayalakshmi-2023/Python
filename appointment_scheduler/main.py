# main.py

from scheduler import (
    add_appointment, remove_appointment,
    edit_appointment, get_schedule,
    get_unique_people
)
from notifier import show_today_appointments

def main():
    while True:
        print("\n📆 Appointment Scheduler")
        print("1. Add Appointment")
        print("2. Remove Appointment")
        print("3. Edit Appointment")
        print("4. View Schedule")
        print("5. View Unique People")
        print("6. Today's Appointments")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time (HH:MM): ")
            person = input("Person: ")
            purpose = input("Purpose: ")
            add_appointment(date, time, person, purpose)
            print("✅ Appointment added.")
        
        elif choice == "2":
            date = input("Date: ")
            time = input("Time: ")
            person = input("Person: ")
            remove_appointment(date, time, person)
            print("🗑️ Appointment removed.")

        elif choice == "3":
            date = input("Date: ")
            time = input("Time: ")
            person = input("Person: ")
            new_time = input("New Time (or Enter to keep same): ") or None
            new_person = input("New Person (or Enter to keep same): ") or None
            new_purpose = input("New Purpose (or Enter to keep same): ") or None
            success = edit_appointment(date, time, person, new_time, new_person, new_purpose)
            print("✅ Updated." if success else "❌ Appointment not found.")

        elif choice == "4":
            schedule = get_schedule()
            print("\n📋 Full Schedule:")
            for date, appts in schedule.items():
                print(f"\n📅 {date}")
                for time, person, purpose in appts:
                    print(f" - ⏰ {time}: {person} ({purpose})")

        elif choice == "5":
            people = get_unique_people()
            print("\n👥 Unique People:", people)

        elif choice == "6":
            show_today_appointments()

        elif choice == "0":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
