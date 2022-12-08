from datetime import datetime

# returns a list of unique challenges
def get_all_unique_challenges(all_data):
    all_challenges = []
    for player, challenges in all_data.items():
        for c in challenges:
            if c not in all_challenges:
                all_challenges.append(c)
    return all_challenges

# returns the ladder on a specific date
def ladder_on_specific_date(all_ladders, target_date_str):
    ladder_list = list(all_ladders.values())
    ladder_list.reverse()
    
    l = ladder_list[0]
    for ladder_date_str, ladder in reversed(all_ladders.items()):
        target_date = datetime.strptime(target_date_str, "%d-%m-%Y")
        ladder_date = datetime.strptime(ladder_date_str, "%d-%m-%Y")
        if ladder_date > target_date:
            break
        else:
            l = ladder
    return l

# gets all the challenges, given 2 players names
def challenges_between_2_players(all_data, player1_name, player2_name):
    challenges = []
    for c in all_data[player1_name]:
        if c["player1_name"] == player2_name or c["player2_name"] == player2_name:
            challenges.append(c)
    return challenges

# returns all the challenges on a specific date
def challenges_on_specific_date(all_data, target_date):
    challenges = []
    all_unique_challenges = get_all_unique_challenges(all_data)
    for c in all_unique_challenges:
        if c["challenge_date"] == target_date:
            challenges.append(c)
    return challenges

# returns all the challenges belonging to a player
def challenges_belonging_to_player(all_data, player_name):
    return all_data[player_name]

# finds and returns the most active player
def most_active_player(all_data):
    player_name = ""
    challenges = []
    challenges_count = 0
    for player, player_challenges in all_data.items():
        if len(player_challenges) > challenges_count:
            player_name = player
            challenges_count = len(player_challenges)
            challenges = player_challenges
    return player_name, challenges

# finds and returns the least active player
def least_active_player(all_data):
    player_name = list(all_data.keys())[0]
    challenges = list(all_data.values())[0]
    challenges_count = len(challenges)
    for player, player_challenges in all_data.items():
        if len(player_challenges) < challenges_count:
            player_name = player
            challenges_count = len(player_challenges)
            challenges = player_challenges
    return player_name, challenges

# finds and returns a list of challenges within a date range.
def challenges_within_date_range(all_data, start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y")

    challenges = []
    all_unique_challenges = get_all_unique_challenges(all_data)
    for c in all_unique_challenges:
        c_date = datetime.strptime(c["challenge_date"], "%d-%m-%Y")
        if c_date >= start_date and c_date <= end_date:
            challenges.append(c)
    return challenges





