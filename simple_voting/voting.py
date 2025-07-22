# voting.py

candidates = {"Alice", "Bob", "Charlie"}
voters = set()
votes = {candidate: 0 for candidate in candidates}

def vote(voter_id, candidate):
    if voter_id in voters:
        return f"❌ Voter '{voter_id}' has already voted."
    if candidate not in candidates:
        return f"❌ Invalid candidate: '{candidate}'."
    
    votes[candidate] += 1
    voters.add(voter_id)
    return f"✅ Vote cast successfully for '{candidate}' by '{voter_id}'."
