# analysis.py
from collections import defaultdict

def monthly_summary(log, month):
    summary = defaultdict(list)
    for date, (temp, humidity, _) in log.items():
        if date.startswith(month):  # e.g. '2025-07'
            summary["temps"].append(temp)
            summary["humidity"].append(humidity)

    if not summary:
        return "📭 No data available for this month."

    avg_temp = sum(summary["temps"]) / len(summary["temps"])
    avg_humidity = sum(summary["humidity"]) / len(summary["humidity"])

    return (
        f"📅 Summary for {month}:\n"
        f" - Days Logged: {len(summary['temps'])}\n"
        f" - Avg Temp: {avg_temp:.1f}°C\n"
        f" - Avg Humidity: {avg_humidity:.1f}%"
    )

def unique_conditions(log):
    return {condition for (_, _, condition) in log.values()}


