students = [
    ("Anu", (85, 90, 88)),
    ("Banu", (78, 82, 80)),
    ("Charu", (92, 88, 95))
]

# Display each student's data
print("Student Score Tracker\n------------------------")

for student in students:
    name, scores = student               # Unpacking
    math, physics, chemistry = scores    # Unpacking inner tuple

    # Access using indexing
    average = sum(scores) / len(scores)

    print(f"Name     : {name}")
    print(f"Math     : {scores[0]}")
    print(f"Physics  : {scores[1]}")
    print(f"Chemistry: {scores[2]}")
    print(f"Average  : {average:.2f}")
    print("-" * 25)

# Demonstrating immutability
students[0][1][0] = 100  # ❌ This would raise a TypeError!
