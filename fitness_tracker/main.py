# main.py

from tracker_ops import add_activity, edit_activity, group_by_type, unique_activity_types, fitness_goal_check
from visuals import calories_by_type

log = []

# Add sample activities
add_activity(log, "2025-07-20", "Running", 30, 300)
add_activity(log, "2025-07-21", "Cycling", 45, 400)
add_activity(log, "2025-07-21", "Yoga", 60, 200)
add_activity(log, "2025-07-22", "Running", 25, 250)

# Edit activity
print(edit_activity(log, "2025-07-21", "Yoga", {"duration": 75, "calories": 250}))

# View unique types
print("\n🏷️ Unique Activities:", unique_activity_types(log))

# Grouped stats
grouped = group_by_type(log)
print("\n📊 Grouped by Activity Type:")
for typ, acts in grouped.items():
    total_cal = sum(a["calories"] for a in acts)
    print(f"- {typ}: {len(acts)} sessions, {total_cal} kcal")

# Check fitness goal
print("\n✅ Goal Check (1000 kcal):")
print(fitness_goal_check(log, 1000))

# Show bar chart
calories_by_type(log)
