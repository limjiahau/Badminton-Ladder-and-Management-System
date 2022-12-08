from datetime import datetime, date
from copy import deepcopy

# given a challenge, check the winner
def check_winner(c):
    scores = c["challenge_scores"].split(" ")
    player1_win = 0
    player2_win = 0
    if c["challenge_scores"] != "":
        for score in scores:
            player1_score_string, player2_score_string = score.split("-")
            player1_score = int(player1_score_string)
            player2_score = int(player2_score_string)
            if player1_score == 21 and player2_score <= 19:
                player1_win += 1
            elif player2_score == 21 and player1_score <= 19:
                player2_win += 1
            elif player1_score >= 20 and player2_score >= 20:
                if player1_score - player2_score == 2:
                    player1_win += 1
                elif player2_score - player1_score == 2:
                    player2_win += 1
    if player1_win == 2:
        return "Player 1"
    elif player2_win == 2:
        return "Player 2"
    else:
        challenge_date = datetime.strptime(c["challenge_date"], "%d-%m-%Y")
        if challenge_date.date() < date.today():
            return "Player 1"
        else:
            return "No winner yet"

def issue_challenge(all_data, ladder, player1_name, player2_name, challenge_date):
    # create the challenge object
    player1_pos = ladder.index(player1_name) + 1
    player2_pos = ladder.index(player2_name) + 1
    challenge_obj = {
        "player1_name": player1_name,
        "player1_pos": player1_pos,
        "player2_name": player2_name,
        "player2_pos": player2_pos,
        "challenge_date": challenge_date,
        "challenge_scores": ""
    }

    # add it to our data
    all_data[player1_name].append(deepcopy(challenge_obj))
    all_data[player2_name].append(deepcopy(challenge_obj))

    # writing back into the files
    with open("data.txt", "a+") as f:
        f.write("\n")
        f.write(f"{player1_name} {player1_pos}/{player2_name} {player2_pos}/{challenge_date}/")
    with open("ladder.txt", "w") as f:
        for line in ladder:
            if ladder.index(line) == len(ladder) - 1:
                f.write(line)
            else:
                f.write(line + "\n")
    return all_data, ladder

def record_result(all_data, ladder, player1_name, player2_name, result):
    # find the challenge object and edit it
    challenge_obj = {}
    challenge_scores = ""
    for c in reversed(all_data[player1_name]):
        if c["player2_name"] == player2_name or c["player1_name"] == player2_name:
            if c["challenge_scores"] == "":
                c["challenge_scores"] = result
            else:
                c["challenge_scores"] = f"{c['challenge_scores']} {result}"
            challenge_obj = c
            challenge_scores = c["challenge_scores"]
            break
    for c in reversed(all_data[player2_name]):
        if c["player1_name"] == player1_name or c["player2_name"] == player1_name:
            if c["challenge_scores"] == "":
                c["challenge_scores"] = result
            else:
                c["challenge_scores"] = f"{c['challenge_scores']} {result}"
            break
 
    # if player1 wins, player1 will move up the ladder
    result = check_winner(challenge_obj)
    if result == "Player 1":
        ladder.remove(challenge_obj["player1_name"])
        ladder.insert(ladder.index(challenge_obj["player2_name"]), challenge_obj["player1_name"])
    
    # writing back into the files
    lines = []
    with open("data.txt") as f:
        lines = f.readlines()
        for l in reversed(lines):
            if player1_name in l and player2_name in l:
                l_list = l.split("/")
                l_list[-1] = challenge_scores + '\n'
                lines[lines.index(l)] = "/".join(l_list)
                break
    with open("data.txt", "w") as f:
        for i, l in enumerate(lines):
            if i == len(lines) - 1:
                f.write(l.strip())
            else:
                f.write(l.strip() + "\n")
    with open("ladder.txt", "w") as f:
        for line in ladder:
            if ladder.index(line) == len(ladder) - 1:
                f.write(line)
            else:
                f.write(line + "\n")

    return all_data, ladder

def join(all_data, ladder, player_name):
    # add the new player to the ladder
    all_data[player_name] = []
    ladder.append(player_name)

    # write back into the files
    with open("data.txt", "a+") as f:
        f.write("\n")
        f.write(f"+{player_name}/{datetime.now().strftime('%d-%m-%Y')}")
    with open("ladder.txt", "w") as f:
        for line in ladder:
            if ladder.index(line) == len(ladder) - 1:
                f.write(line)
            else:
                f.write(line + "\n")

    return all_data, ladder

def withdraw(all_data, ladder, player_name):
    # remove player from the ladder
    if player_name in all_data:
        del all_data[player_name]
    player_pos = ladder.index(player_name) + 1
    ladder.remove(player_name)

    # write back into the files
    with open("data.txt", "a+") as f:
        f.write("\n")
        f.write(f"-{player_name} {player_pos}/{datetime.now().strftime('%d-%m-%Y')}")
    with open("ladder.txt", "w") as f:
        for line in ladder:
            if ladder.index(line) == len(ladder) - 1:
                f.write(line)
            else:
                f.write(line + "\n")
    return all_data, ladder

def forfeit_pending_challenge(all_data, ladder, player1_name, player2_name):
    # find the challenge object and remove it
    challenge_obj = {}
    challenge_scores = ""
    for c in reversed(all_data[player1_name]):
        if c["player2_name"] == player2_name or c["player1_name"] == player2_name:
            all_data[player1_name].remove(c)
            break
    for c in reversed(all_data[player2_name]):
        if c["player1_name"] == player1_name or c["player2_name"] == player1_name:
            all_data[player2_name].remove(c)
            break
    # writing back into the files
    lines = []
    with open("data.txt") as f:
        lines = f.readlines()
        for l in reversed(lines):
            if player1_name in l and player2_name in l:
                lines.remove(l)
                break
    with open("data.txt", "w") as f:
        for i, l in enumerate(lines):
            if i == len(lines) - 1:
                f.write(l.strip())
            else:
                f.write(l.strip() + "\n")

    return all_data, ladder
