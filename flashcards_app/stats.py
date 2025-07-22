# stats.py

def display_stats(stats):
    total = stats["correct"] + stats["incorrect"]
    if total == 0:
        return "📊 No quiz taken yet."
    return (
        f"📈 Stats:\n"
        f"Correct: {stats['correct']}\n"
        f"Incorrect: {stats['incorrect']}\n"
        f"Accuracy: {stats['correct'] / total * 100:.2f}%"
    )

def reset_stats(stats):
    stats["correct"] = 0
    stats["incorrect"] = 0
    return "🔄 Stats reset."
