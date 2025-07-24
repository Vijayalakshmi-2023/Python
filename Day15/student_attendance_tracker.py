import logging

# Setup logging for absentees
logging.basicConfig(filename="absentees.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class OverAttendanceError(Exception):
    """Raised when attendance exceeds maximum allowed days."""
    pass

def track_attendance(max_days=30):
    print("📋 Student Attendance Tracker")
    print("Enter 'done' to stop.\n")

    student_records = {}

    while True:
        try:
            roll = input("Enter student roll number: ").strip()

            if roll.lower() == 'done':
                break

            if not roll.isdigit():
                raise ValueError("Roll number must be numeric.")

            days_attended_input = input(f"Enter days attended (max {max_days}) for roll {roll}: ").strip()

            if not days_attended_input.isdigit():
                raise ValueError("Days attended must be a number.")

            days_attended = int(days_attended_input)

            if days_attended > max_days:
                raise OverAttendanceError(f"Attendance {days_attended} exceeds max of {max_days} days.")

            student_records[roll] = days_attended

            if days_attended == 0:
                logging.info(f"Roll {roll} was absent for all {max_days} days.")

        except OverAttendanceError as oae:
            print(f"❌ Error: {oae}")
        except ValueError as ve:
            print(f"❌ Error: {ve}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        else:
            print(f"✅ Recorded: Roll {roll} - {days_attended} days")
        print()

    # Summary Report
    print("\n📊 Attendance Summary")
    for roll, days in student_records.items():
        print(f"Roll {roll}: {days} day(s) present")

# Run the tracker
if __name__ == "__main__":
    track_attendance()
