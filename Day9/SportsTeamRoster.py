# Sample team roster data as a list of tuples (player_id, name, (position, goals))
team_roster = [
    (1, "Arun", ("Striker", 12)),
    (2, "Aravind", ("Midfielder", 5)),
    (3, "David", ("Striker", 8)),
    (4, "Ram", ("Defender", 3)),
    (5, "Akash", ("Striker", 15)),
    (6, "Ravi", ("Midfielder", 7)),
    (7, "Prem", ("Goalkeeper", 0)),
    (8, "Sundar", ("Striker", 18)),
    (9, "Mohammed", ("Defender", 2)),
    (10, "Prakash", ("Midfielder", 10))
]

# 1. Display players with more than 10 goals
def display_top_scorers():
    print("Players with more than 10 goals:")
    print("-" * 30)
    for player in team_roster:
        player_id, name, (position, goals) = player  # Unpacking the tuple
        if goals > 10:
            print(f"Player ID: {player_id}, Name: {name}, Position: {position}, Goals: {goals}")
    print("-" * 30)

# 2. Count how many strikers are in the team
def count_strikers():
    striker_count = 0
    for player in team_roster:
        _, _, (position, _) = player  # Unpacking the tuple and ignoring player_id and name
        if position == "Striker":
            striker_count += 1
    print(f"Total number of strikers in the team: {striker_count}")

# 3. Create team summary using tuple packing and unpacking
def team_summary():
    total_players = len(team_roster)
    strikers = [player for player in team_roster if player[2][0] == "Striker"]
    strikers_count = len(strikers)
    top_scorer = max(team_roster, key=lambda player: player[2][1])  # Find player with most goals
    
    _, top_scorer_name, (_, top_scorer_goals) = top_scorer
    print(f"Total Players: {total_players}")
    print(f"Total Strikers: {strikers_count}")
    print(f"Top Scorer: {top_scorer_name} with {top_scorer_goals} goals")

# Testing the functions
display_top_scorers()  # Display players with more than 10 goals
count_strikers()  # Count the number of strikers
team_summary()  # Display team summary