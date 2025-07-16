# Format: {candidate_name: vote_count}
votes = {
    "Anu": 0,
    "Banu": 0,
    "Charu": 0
}
# Increment vote for a candidate
def vote(candidate_name):
    if candidate_name in votes:
        votes[candidate_name] = votes.get(candidate_name, 0) + 1
        print(f"Vote for {candidate_name} counted. Current vote count: {votes[candidate_name]}")
    else:
        print(f"Invalid vote: {candidate_name} is not a valid candidate.")

# Show the winner by finding the candidate with the maximum votes
def show_winner():
    winner = max(votes, key=votes.get)
    print(f"\nThe winner is: {winner} with {votes[winner]} votes.")

# Detect invalid votes
def detect_invalid_vote(candidate_name):
    if candidate_name not in votes:
        print(f"Invalid vote: {candidate_name} is not in the candidate list.")
    else:
        print(f"Vote for {candidate_name} is valid.")

# Simulating the voting process
vote("Anu")    
vote("Banu")      
vote("Charu")  
vote("Diya")     # Invalid vote (not in candidate list)

# Show the winner
show_winner()
