# Survey Response Filter

# Initial set of valid response IDs
response_ids = {"R001", "R002", "R003", "R004"}

# Add new responses using update()
new_responses = {"R005", "R006", "R007"}
response_ids.update(new_responses)
print("After adding new responses:", response_ids)

# Invalid responses to remove
invalid_responses = {"R002", "R008"}  # R008 does not exist

# Track removed responses
removed_responses = set()

# Remove invalid responses using remove() and discard()
for resp in invalid_responses:
    try:
        response_ids.remove(resp)  # remove() raises KeyError if not found
        removed_responses.add(resp)
        print(f"Removed response: {resp}")
    except KeyError:
        print(f"Response {resp} not found with remove(), trying discard()")
        # discard() won't raise error, but we track only if removed
        if resp in response_ids:
            response_ids.discard(resp)
            removed_responses.add(resp)
            print(f"Discarded response: {resp}")
        else:
            print(f"Response {resp} not present; nothing removed.")

print("\nResponses after removals:", response_ids)
print("Removed responses:", removed_responses)

# Use pop() to test random removal
random_response = response_ids.pop()
print(f"\nRandomly removed response using pop(): {random_response}")
print("Responses now:", response_ids)
