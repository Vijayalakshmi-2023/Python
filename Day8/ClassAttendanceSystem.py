# Class Attendance System

# Master list of students
master_students = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]

def get_present_students():
    print("Enter present students' names separated by commas:")
    input_names = input().strip()
    # Split by comma, strip spaces, capitalize names for uniformity
    present_list = [name.strip().title() for name in input_names.split(",")]
    # Remove duplicates by converting to set and back to list
    present_unique = list(set(present_list))
    return present_unique

def main():
    print("🎓 Class Attendance System\n")
    print(f"Master List of Students ({len(master_students)}): {master_students}\n")
    
    present_students = get_present_students()
    print(f"\n✅ Present Students ({len(present_students)}): {present_students}")
    
    # Calculate absentees by set difference
    absentees = list(set(master_students) - set(present_students))
    
    print(f"\n❌ Absent Students ({len(absentees)}): {absentees}")

if __name__ == "__main__":
    main()
