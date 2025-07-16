feedback_data = {}
# Add customer feedback
def add_feedback(customer_id, feedback, rating):
    feedback_data[customer_id] = {"feedback": feedback, "rating": rating}
    print(f"Feedback from customer {customer_id} added.")

# Compute average rating using .values()
def average_rating():
    ratings = [data["rating"] for data in feedback_data.values()]
    if ratings:
        return sum(ratings) / len(ratings)
    return 0

# Count number of positive and negative feedback
def feedback_summary():
    summary = {"positive": 0, "negative": 0}
    for data in feedback_data.values():
        if data["rating"] >= 4:
            summary["positive"] += 1
        else:
            summary["negative"] += 1
    return summary

# Extract customers with rating > 4 using dictionary comprehension
def high_rated_customers():
    return {customer_id: data for customer_id, data in feedback_data.items() if data["rating"] > 4}

# Display feedback
def show_feedback():
    print("\nCustomer Feedback:")
    if not feedback_data:
        print("  No feedback available.")
    for customer_id, data in feedback_data.items():
        print(f"  Customer {customer_id}: {data['feedback']} (Rating: {data['rating']})")
# Add feedback
add_feedback(101, "Great service, will come again!", 5)
add_feedback(102, "Not satisfied with the product.", 2)
add_feedback(103, "Good, but delivery was delayed.", 3)
add_feedback(104, "Excellent! Very happy with my purchase.", 5)

# Average rating
print("\nAverage Rating:", average_rating())

# Feedback summary (positive/negative count)
summary = feedback_summary()
print("\nFeedback Summary:")
print(f"  Positive: {summary['positive']}")
print(f"  Negative: {summary['negative']}")

# Customers with rating > 4
high_rated = high_rated_customers()
print("\nCustomers with Rating > 4:")
for customer_id, data in high_rated.items():
    print(f"  Customer {customer_id}: {data['feedback']}")

# Show all feedback
show_feedback()
