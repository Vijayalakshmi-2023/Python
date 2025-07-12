def collect_feedback():
    feedbacks = []
    print("Enter feedback one by one (type 'done' to finish):")
    while True:
        fb = input("Feedback: ").strip()
        if fb.lower() == "done":
            break
        if fb:
            feedbacks.append(fb)
        else:
            print("❌ Feedback cannot be empty.")
    return feedbacks

def count_sentiments(feedbacks):
    counts = {"good": 0, "bad": 0, "average": 0}

    for fb in feedbacks:
        fb_lower = fb.lower()
        if "good" in fb_lower:
            counts["good"] += 1
        elif "bad" in fb_lower:
            counts["bad"] += 1
        elif "average" in fb_lower:
            counts["average"] += 1

    return counts

def main():
    print("=== Feedback Collector ===")
    feedbacks = collect_feedback()

    if not feedbacks:
        print("No feedback collected.")
        return

    counts = count_sentiments(feedbacks)

    print("\n=== Sentiment Counts ===")
    print(f"Good: {counts['good']}")
    print(f"Bad: {counts['bad']}")
    print(f"Average: {counts['average']}")

if __name__ == "__main__":
    main()
