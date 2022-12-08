from datetime import datetime
from copy import deepcopy

# reads from data.txt and load it into a dictionary
def load_data():
    all_data = {}
    with open("data.txt") as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

        for line in lines:
            # splitting each line by "/"
            l = line.split("/")

            # if length is 2, it is a join or withdraw action
            if len(l) == 2:
                player = l[0]
                action_date_string = l[1]
                action_type = player[0]
                player_name = player[1:]
                # add the player to the dict if it is a join
                if action_type == "+":
                    if player_name not in all_data:
                        all_data[player_name] = []
                # remove the player from dict if it is a withdraw
                elif action_type == "-":
                    player_name = player_name.rsplit(" ", 1)[0]
                    if player_name in all_data:
                        del all_data[player_name]
            # if length is 4, it is a challenge
            elif len(l) == 4:
                player1 = l[0]
                player1_name, player1_pos = player1.rsplit(" ", 1)
                player2 = l[1]
                player2_name, player2_pos = player2.rsplit(" ", 1)
                challenge_date_string = l[2]
                challenge_scores = l[3]
                
                # add players to dict if not already in
                if player1_name not in all_data:
                    all_data[player1_name] = []
                if player2_name not in all_data:
                    all_data[player2_name] = []

                # create the challenge object
                challenge_obj = {
                    "player1_name": player1_name,
                    "player1_pos": player1_pos,
                    "player2_name": player2_name,
                    "player2_pos": player2_pos,
                    "challenge_date": challenge_date_string,
                    "challenge_scores": challenge_scores
                }

                # append to both players.
                # deepcopy is used to avoid pass by reference on the objects
                all_data[player1_name].append(deepcopy(challenge_obj))
                all_data[player2_name].append(deepcopy(challenge_obj))

        
    return all_data

# read ladder.txt
def load_ladder():
    ladder = []
    with open("ladder.txt") as f:
        ladder = [x.strip() for x in f.readlines()]
    return ladder

# consolidates and calculate all the previous ladders.
def load_ladder_by_date():
    ladder_by_date = {}
    with open("data.txt") as data_f, open("ladder.txt") as ladder_f:
        current_ladder = [x.strip() for x in ladder_f.readlines()]
        current_date_string = datetime.strftime(datetime.now(), "%d-%m-%Y")
        ladder_by_date[current_date_string] = current_ladder[:]

        lines = [l.strip() for l in data_f.readlines()]
        for i in reversed(range(len(lines))):
            line = lines[i]
            l = line.split("/")
            # if length is 2, it is a join/withdraw action
            if len(l) == 2:
                player = l[0]
                date_string = l[1]
                action_type = player[0]
                player_name = player[1:]

                # if it was a join action, we now remove the player to get the previous ladder
                if action_type == "+":
                    current_ladder.remove(player_name)
                # if it was a leave action, we add back the player
                elif action_type == "-":
                    player_pos = player_name.rsplit(" ", 1)[1]
                    player_name = player_name.rsplit(" ", 1)[0]
                    current_ladder.insert(int(player_pos) - 1, player_name)

            # if length is 4, it is a challenge.
            elif len(l) == 4:
                player1 = l[0]
                player1_name, player1_pos = player1.rsplit(" ", 1)
                player2 = l[1]
                player2_name, player2_pos = player2.rsplit(" ", 1)
                date_string = l[2]
                challenge_scores = l[3]

                # if the positions of the players are different, means that player1 won, and should revert positions
                if current_ladder.index(player1_name) != int(player1_pos) - 1 and current_ladder.index(player2_name) != int(player2_pos) - 1:
                    current_ladder.remove(player1_name)
                    current_ladder.insert(int(player1_pos) - 1, player1_name)
            
            # get the date to save the ladder by
            
            if i != 0:
                # if it is not the first item, we use the date from the previous item
                previous_l = lines[i-1].split("/")
                if len(previous_l) == 2:
                    previous_date_string = previous_l[1]
                elif len(previous_l) == 4:
                    previous_date_string = previous_l[2]
            else:
                # if it is the first item, we subtract 1 year
                date_list = date_string.split("-")
                date_year = int(date_list[-1])
                new_date_year = date_year - 1
                date_list[-1] = str(new_date_year)
                previous_date_string = "-".join(date_list)

            # save the ladder into the dictionary
            if previous_date_string not in ladder_by_date:
                ladder_by_date[previous_date_string] = current_ladder[:]

    return ladder_by_date

