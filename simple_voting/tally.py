# tally.py

from voting import votes

def tally_results():
    print("\n🗳 Voting Results:")
    for candidate, count in votes.items():
        print(f"{candidate:<10}: {count} vote(s)")

def announce_winner():
    max_votes = max(votes.values())
    winners = [c for c, v in votes.items() if v == max_votes]

    if len(winners) == 1:
        print(f"\n🏆 Winner: {winners[0]} with {max_votes} votes.")
    else:
        print(f"\n🤝 It's a tie between: {', '.join(winners)} with {max_votes} votes each.")
