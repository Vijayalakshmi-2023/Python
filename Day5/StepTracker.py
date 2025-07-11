total_steps = 0
day = 1
entries = 0  # Counts valid entries (non-zero)

while day <= 7:
    try:
        steps = int(input(f"Enter steps walked on day {day}: "))
    except ValueError:
        print("❌ Please enter a valid integer.")
        continue

    if steps == 0:
        print("⚠️ Step count zero, skipping this day.")
        day += 1
        continue  # Skip zero entries but count the day

    total_steps += steps
    entries += 1
    day += 1
else:
    if entries > 0:
        average = total_steps / entries
        print(f"\n✅ Total steps: {total_steps}")
        print(f"✅ Average steps per day (excluding zeros): {average:.2f}")
    else:
        print("\n⚠️ No valid step entries recorded.")
