# Simple Poll App
responses = []

def ask_poll():
    print("📊 POLL: Do you support the new policy? (Yes/No)")
    while True:
        answer = input("Enter response (or type 'done' to finish): ").strip().lower()
        
        if answer == 'done':
            break
        elif answer == 'yes' or answer == 'no':
            responses.append(answer)
        else:
            print("❌ Invalid input. Please enter 'Yes' or 'No'.")

def analyze_results():
    yes_count = responses.count('yes')
    no_count = responses.count('no')
    total = yes_count + no_count

    print("\n📝 Poll Results:")
    print(f"Total responses: {total}")
    print(f"✅ Yes: {yes_count}")
    print(f"❌ No: {no_count}")

# Run the poll
ask_poll()
analyze_results()
