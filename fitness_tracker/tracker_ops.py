# tracker_ops.py

def add_activity(log, date, activity_type, duration, calories):
    entry = {
        "date": date,
        "type": activity_type,
        "duration": duration,
        "calories": calories
    }
    log.append(entry)
    return f"✅ Added activity: {activity_type} on {date}"

def edit_activity(log, date, activity_type, new_data):
    for activity in log:
        if activity["date"] == date and activity["type"] == activity_type:
            activity.update(new_data)
            return f"✏️ Updated activity: {activity_type} on {date}"
    return "❌ Activity not found."

def group_by_type(log):
    grouped = {}
    for act in log:
        grouped.setdefault(act["type"], []).append(act)
    return grouped

def unique_activity_types(log):
    return {act["type"] for act in log}

def fitness_goal_check(log, goal_calories):
    total = sum(act["calories"] for act in log)
    if total >= goal_calories:
        return f"🎯 Goal achieved! Total calories burned: {total}"
    return f"🚧 Keep going! Calories burned: {total}/{goal_calories}"
