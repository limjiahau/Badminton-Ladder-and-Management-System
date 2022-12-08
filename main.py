from load import *
from actions import *
from queries import *
from datetime import datetime, date
import turtle

# load all the required data
all_data = load_data()
current_ladder = load_ladder()
all_ladders = load_ladder_by_date()

# check if given challenge is completed
def is_challenge_completed(c):
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
    if player1_win == 2 or player2_win == 2:
        return True
    else:
        challenge_date = datetime.strptime(c["challenge_date"], "%d-%m-%Y")
        if challenge_date.date() < date.today():
            return True

# return all completed challenges
def get_all_completed_challenges():
    all_challenges = []
    for player, challenges in all_data.items():
        for c in challenges:
            if c not in all_challenges and is_challenge_completed(c):
                all_challenges.append(c)
    all_challenges.sort(key=lambda x: datetime.strptime(x["challenge_date"], "%d-%m-%Y"))
    return all_challenges

# return all pending challenges
def get_all_pending_challenges():
    pending_challenges = []
    for player, challenges in all_data.items():
        for c in challenges:
            if c not in pending_challenges and not is_challenge_completed(c):
                pending_challenges.append(c)
    pending_challenges.sort(key=lambda x: datetime.strptime(x["challenge_date"], "%d-%m-%Y"))
    return pending_challenges

buttons = {}

# initialize turtle
screen = turtle.Screen()
screen.setup(width=1200, height=600, startx=0, starty=0)
screen.colormode(255)
screen.tracer(0)

# draws the main screen
def draw():
    screen.reset()

    # draw my name
    turtle.up()
    turtle.goto(400,-220)
    turtle.down()
    turtle.write("Done by: Lim Jia Hau (U2020043A)", False, align="center", font=("Arial", 14, "bold"))
    turtle.up()
    turtle.goto(292,-240)
    turtle.down()
    turtle.write("Class: PT1", False, align="center", font=("Arial", 14, "bold"))

    # draw the title
    turtle.up()
    turtle.goto(0, 250)
    turtle.down()
    turtle.write("Badminton Ladder", False, align="center", font=("Arial", 20, "bold"))

    # draw the ladder
    turtle.up()
    turtle.goto(-350, 200)
    turtle.down()
    turtle.write("Ladder", False, align="center", font=("Arial", 14, "bold"))

    turtle.fillcolor(255, 255, 176)
    for i, player in enumerate(current_ladder):
        turtle.up()
        turtle.goto(-450, 200-i*25)
        turtle.down()

        turtle.begin_fill()
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(-450, 175-i*25)
        turtle.down()
        turtle.write(f"   {(i+1)}.  {player}", False, align="Left", font=("Arial", 14, "normal"))
    turtle.fillcolor(0, 0, 0)

    # draw the actions
    turtle.up()
    turtle.goto(-100, 200)
    turtle.down()
    turtle.write("Select Action", False, align="center", font=("Arial", 14, "bold"))
    list_of_actions = ["Issue Challenge", "Record Result", "Withdraw", "Join", "Forfeit Challenge"]

    turtle.fillcolor(207, 236, 207)
    for i, action in enumerate(list_of_actions):
        turtle.up()
        turtle.goto(-200, 200-i*25)
        turtle.down()

        turtle.begin_fill()
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(-200, 175-i*25)
        turtle.down()
        turtle.write("   " + action, False, align="Left", font=("Arial", 14, "normal"))

        buttons[action] = [(-200, 200-i*25), (0, 175-i*25)]
    turtle.fillcolor(0, 0, 0)

    # draw the queries
    turtle.up()
    turtle.goto(-65, 25)
    turtle.down()
    turtle.write("Select Query", False, align="center", font=("Arial", 14, "bold"))
    list_of_queries = ["Ladder on specific date", "Challenges between 2 players", "Challenges on specific date", "Challenges belonging to player", "Most active player", "Least active player", "Challenges within date range"]

    turtle.fillcolor(204, 236, 239)
    for i, query in enumerate(list_of_queries):
        turtle.up()
        turtle.goto(-200, 25-i*25)
        turtle.down()

        turtle.begin_fill()
        turtle.forward(280)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(280)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(-200, -i*25)
        turtle.down()
        turtle.write("   " + query, False, align="Left", font=("Arial", 14, "normal"))\

        buttons[query] = [(-200, 25-i*25), (70, -i*25)]
    turtle.fillcolor(0, 0, 0)

    # draw the last 3 completed challenges
    all_completed_challenges = get_all_completed_challenges()
    turtle.up()
    turtle.goto(330, 200)
    turtle.down()
    turtle.write("Last 3 Completed Challenges", False, align="center", font=("Arial", 14, "bold"))

    for i in range(1, 4):
        turtle.up()
        turtle.goto(130, 250-i*50)
        turtle.down()

        turtle.fillcolor(192, 179, 215)
        turtle.begin_fill()
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(130, 225-i*50)
        turtle.down()

        turtle.fillcolor(221, 212, 232)
        turtle.begin_fill()
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(130, 225-i*50)
        turtle.down()
        turtle.write(f"   {all_completed_challenges[-i]['player1_name']} vs {all_completed_challenges[-i]['player2_name']} @ {all_completed_challenges[-i]['challenge_date']}", False, align="Left", font=("Arial", 14, "normal"))

        turtle.up()
        turtle.goto(130, 200-i*50)
        turtle.down()
        turtle.write(f"   --> {all_completed_challenges[-i]['challenge_scores']}", False, align="Left", font=("Arial", 14, "normal"))
    turtle.fillcolor(0, 0, 0)

    # draw pending challenges
    pending_challenges = get_all_pending_challenges()

    turtle.up()
    turtle.goto(290, 0)
    turtle.down()
    turtle.write("Pending Challenges", False, align="center", font=("Arial", 14, "bold"))

    if len(pending_challenges) == 0:
        turtle.up()
        turtle.goto(130, 0)
        turtle.down()

        turtle.fillcolor(251, 182, 209)
        turtle.begin_fill()
        turtle.forward(315)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(315)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(130, -25)
        turtle.down()
        turtle.write("   There are no pending challenges!", False, align="Left", font=("Arial", 14, "normal"))

    else:
        for i in range(1, len(pending_challenges) + 1):
            turtle.up()
            turtle.goto(130, 50-i*50)
            turtle.down()

            turtle.fillcolor(251, 182, 209)
            turtle.begin_fill()
            turtle.forward(400)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
            turtle.forward(400)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
            turtle.end_fill()

            turtle.up()
            turtle.goto(130, 25-i*50)
            turtle.down()

            turtle.fillcolor(253, 222, 238)
            turtle.begin_fill()
            turtle.forward(400)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
            turtle.forward(400)
            turtle.right(90)
            turtle.forward(25)
            turtle.right(90)
            turtle.end_fill()

            turtle.up()
            turtle.goto(130, 25-i*50)
            turtle.down()
            turtle.write(f"   {pending_challenges[-i]['player1_name']} vs {pending_challenges[-i]['player2_name']} @ {pending_challenges[-i]['challenge_date']}", False, align="Left", font=("Arial", 14, "normal"))

            turtle.up()
            turtle.goto(130, -i*50)
            turtle.down()
            turtle.write(f"   --> {pending_challenges[-i]['challenge_scores']}", False, align="Left", font=("Arial", 14, "normal"))

    turtle.fillcolor(0, 0, 0)

    turtle.up()
    turtle.goto(-600, -265)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.end_fill()

    turtle.pencolor(255, 255, 255)
    turtle.up()
    turtle.goto(0, -290)
    turtle.down()
    turtle.write("Use your mouse to select an action or query", False, align="center", font=("Arial", 14, "normal"))
    turtle.pencolor(0, 0, 0)

    turtle.hideturtle()
    screen.update()
    screen.onclick(execute_click)

# draw the user feedback at the bottom of the screen
def write_user_feedback(message):
    turtle.up()
    turtle.goto(-600, -265)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.end_fill()

    turtle.pencolor(255, 255, 255)
    turtle.up()
    turtle.goto(0, -290)
    turtle.down()
    turtle.write(message, False, align="center", font=("Arial", 14, "normal"))
    turtle.pencolor(0, 0, 0)

    turtle.hideturtle()
    screen.update()

# draw the ladder in the middle
def draw_ladder(heading, ladder):
    screen.reset()

    turtle.up()
    turtle.goto(0, 250)
    turtle.down()
    turtle.write("Badminton Ladder", False, align="center", font=("Arial", 20, "bold"))

    turtle.up()
    turtle.goto(0, 200)
    turtle.down()
    turtle.write(heading, False, align="center", font=("Arial", 14, "bold"))

    turtle.fillcolor(255, 255, 176)
    for i, player in enumerate(ladder):
        turtle.up()
        turtle.goto(-100, 200-i*25)
        turtle.down()

        turtle.begin_fill()
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(-100, 175-i*25)
        turtle.down()
        turtle.write(f"   {(i+1)}.  {player}", False, align="Left", font=("Arial", 14, "normal"))
    turtle.fillcolor(0, 0, 0)

    turtle.up()
    turtle.goto(-600, -265)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.end_fill()
    
    turtle.pencolor(255, 255, 255)
    turtle.up()
    turtle.goto(0, -290)
    turtle.down()
    turtle.write("Click anywhere to return", False, align="center", font=("Arial", 14, "normal"))
    turtle.pencolor(0, 0, 0)

    turtle.hideturtle()
    screen.update()

    def click_to_return(x, y):
        draw()

    screen.onclick(click_to_return)

# draw the challenges in the middle
def draw_challenges(heading, challenges):
    screen.reset()

    turtle.up()
    turtle.goto(0, 250)
    turtle.down()
    turtle.write("Badminton Ladder", False, align="center", font=("Arial", 20, "bold"))

    turtle.up()
    turtle.goto(0, 200)
    turtle.down()
    turtle.write(heading, False, align="center", font=("Arial", 14, "bold"))

    for i, c in enumerate(challenges):
        turtle.up()
        turtle.goto(-180, 200-i*50)
        turtle.down()

        turtle.fillcolor(253, 202, 162)
        turtle.begin_fill()
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(-180, 175-i*50)
        turtle.down()

        turtle.fillcolor(254, 235, 201)
        turtle.begin_fill()
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.end_fill()

        turtle.up()
        turtle.goto(-180, 175-i*50)
        turtle.down()
        turtle.write(f"   {c['player1_name']} vs {c['player2_name']} @ {c['challenge_date']}", False, align="Left", font=("Arial", 14, "normal"))

        turtle.up()
        turtle.goto(-180, 150-i*50)
        turtle.down()
        turtle.write(f"   --> {c['challenge_scores']}", False, align="Left", font=("Arial", 14, "normal"))

    turtle.fillcolor(0, 0, 0)
    turtle.up()
    turtle.goto(-600, -265)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(1200)
    turtle.right(90)
    turtle.forward(35)
    turtle.right(90)
    turtle.end_fill()
    
    turtle.pencolor(255, 255, 255)
    turtle.up()
    turtle.goto(0, -290)
    turtle.down()
    turtle.write("Click anywhere to return", False, align="center", font=("Arial", 14, "normal"))
    turtle.pencolor(0, 0, 0)

    turtle.hideturtle()
    screen.update()

    def click_to_return(x, y):
        draw()

    screen.onclick(click_to_return)

# click handler
def execute_click(x, y):
    global all_data, current_ladder
    for key, value in buttons.items():
        top_right, bottom_left = value

        # check click is within which box
        if x > top_right[0] and x < bottom_left[0] and y < top_right[1] and y > bottom_left[1]:

            if key == "Issue Challenge":
                user_input = screen.textinput("Issue Challenge", "Please enter name of Player 1, name of Player 2, and the challenge date (DD-MM-YYYY)\nPlease use commas to separate them, e.g. 'S Praneeth, TW Wang, 29-03-2021'")
                if not user_input:
                    break
                # checking if inputs are valid
                try:
                    player1_name, player2_name, challenge_date = [x.strip() for x in user_input.split(",")]
                except ValueError:
                    write_user_feedback("Incorrect input format!")
                    break
                if player1_name not in current_ladder:
                    write_user_feedback(f"{player1_name} doesn't exist!")
                    break
                if player2_name not in current_ladder:
                    write_user_feedback(f"{player2_name} doesn't exist!")
                    break
                # checking if player1 can challenge player2
                player1_pos = current_ladder.index(player1_name)
                player2_pos = current_ladder.index(player2_name)
                if player1_pos <= player2_pos or player1_pos - player2_pos > 3:
                    write_user_feedback(f"{player1_name} is not allowed to challenge {player2_name}")
                    break
                pending_challenges = get_all_pending_challenges()
                for c in pending_challenges:
                    if c["player1_name"] == player1_name or c["player2_name"] == player1_name:
                        write_user_feedback(f"{player1_name} already has a pending challenge!")
                        return
                    elif c["player1_name"] == player2_name or c["player2_name"] == player2_name:
                        write_user_feedback(f"{player2_name} already has a pending challenge!")
                        return
                try:
                    datetime.strptime(challenge_date, "%d-%m-%Y")
                except ValueError:
                    write_user_feedback(f"{challenge_date} is an invalid date!")
                    break

                # execute the action
                all_data, current_ladder = issue_challenge(all_data, current_ladder, player1_name, player2_name, challenge_date)

                # draw the screen
                draw()

            elif key == "Record Result":
                user_input = screen.textinput("Record Result", "Please enter name of Player 1, name of Player 2, and the challenge score (XX-YY)\nPlease use commas to separate them, e.g. 'S Praneeth, TW Wang, 21-6'")
                if not user_input:
                    break
                # checking if inputs are valid
                try:
                    player1_name, player2_name, challenge_score = [x.strip() for x in user_input.split(",")]
                except ValueError:
                    write_user_feedback("Incorrect input format!")
                    break
                if player1_name not in current_ladder:
                    write_user_feedback(f"{player1_name} doesn't exist!")
                    break
                if player2_name not in current_ladder:
                    write_user_feedback(f"{player2_name} doesn't exist!")
                    break
                pending_challenges = get_all_pending_challenges()
                is_challenge_pending = False
                for c in pending_challenges:
                    if c["player1_name"] == player1_name and c["player2_name"] == player2_name or c["player2_name"] == player1_name and c["player1_name"] == player2_name:
                        is_challenge_pending = True
                        break
                if not is_challenge_pending:
                    write_user_feedback(f"There are no pending challenges between {player1_name} and {player2_name}")
                    break

                # checking if the score is valid
                player1_score_string, player2_score_string = challenge_score.split("-")
                player1_score = int(player1_score_string)
                player2_score = int(player2_score_string)
                is_score_valid = False
                if player1_score == 21 and player2_score <= 19:
                    is_score_valid = True
                elif player2_score == 21 and player1_score <= 19:
                    is_score_valid = True
                elif player1_score >= 20 and player2_score >= 20:
                    if player1_score - player2_score == 2:
                        is_score_valid = True
                    elif player2_score - player1_score == 2:
                        is_score_valid = True
                if not is_score_valid:
                    write_user_feedback(f"{challenge_score} is not a valid score!")
                    break

                # execute the action
                all_data, current_ladder = record_result(all_data, current_ladder, player1_name, player2_name, challenge_score)

                # draw the screen
                draw()

            elif key == "Join":
                player_name = screen.textinput("Join", "Please enter name of new player.")
                # checking if inputs are valid
                if not player_name:
                    break
                player_name = player_name.strip()
                if player_name in current_ladder:
                    write_user_feedback(f"{player_name} already exists!")
                    break
                # execute the action
                all_data, current_ladder = join(all_data, current_ladder, player_name)

                # draw the screen
                draw()
                
            elif key == "Withdraw":
                player_name = screen.textinput("Withdraw", "Please enter name of withdrawing player.")
                # checking if inputs are valid
                if not player_name:
                    break
                player_name = player_name.strip()
                if player_name not in current_ladder:
                    write_user_feedback(f"{player_name} doesn't exist!")
                    break

                # check if there are any pending challenges under this player. If there are, forfeit them
                pending_challenges = get_all_pending_challenges()
                for c in pending_challenges:
                    if c["player1_name"] == player_name or c["player2_name"] == player_name:
                        all_data, current_ladder = forfeit_pending_challenge(all_data, current_ladder, c["player1_name"], c["player2_name"])

                # execute the action
                all_data, current_ladder = withdraw(all_data, current_ladder, player_name)
                
                # draw the screen
                draw()

            elif key == "Forfeit Challenge":
                user_input = screen.textinput("Forfeit Challenge", "Please enter name of Player 1 and name of Player 2. Must be a pending challenge.\nPlease use commas to separate them, e.g. 'S Praneeth, TW Wang'")
                if not user_input:
                    break
                # checking if inputs are valid
                try:
                    player1_name, player2_name = [x.strip() for x in user_input.split(",")]
                except ValueError:
                    write_user_feedback("Incorrect input format!")
                    break
                if player1_name not in current_ladder:
                    write_user_feedback(f"{player1_name} doesn't exist!")
                    break
                if player2_name not in current_ladder:
                    write_user_feedback(f"{player2_name} doesn't exist!")
                    break
                pending_challenges = get_all_pending_challenges()
                is_challenge_pending = False
                for c in pending_challenges:
                    if c["player1_name"] == player1_name and c["player2_name"] == player2_name or c["player2_name"] == player1_name and c["player1_name"] == player2_name:
                        is_challenge_pending = True
                        break
                if not is_challenge_pending:
                    write_user_feedback(f"There are no pending challenges between {player1_name} and {player2_name}")
                    break

                # execute the action
                all_data, current_ladder = forfeit_pending_challenge(all_data, current_ladder, player1_name, player2_name)

                # draw the screen
                draw()


            elif key == "Ladder on specific date":
                target_date = screen.textinput("Ladder on specific date", "Please enter the date that you wish to view the ladder (DD-MM-YYYY)")
                # checking if inputs are valid
                if not target_date:
                    break
                target_date = target_date.strip()
                try:
                    datetime.strptime(target_date, "%d-%m-%Y")
                except ValueError:
                    write_user_feedback(f"{target_date} is an invalid date!")
                    break
                
                # execute the query
                ladder_result = ladder_on_specific_date(all_ladders, target_date)

                # draw the ladder in the middle
                draw_ladder(f"Ladder on {target_date}", ladder_result)


            elif key == "Challenges between 2 players":
                user_input = screen.textinput("Challenges between 2 players", "Please enter name of Player 1 and Player 2, separated with a comma.\ne.g. 'S Praneeth, J Christie'")
                if not user_input:
                    break
                # checking if inputs are valid
                try:
                    player1_name, player2_name = [x.strip() for x in user_input.split(",")]
                except ValueError:
                    write_user_feedback("Incorrect input format!")
                    break
                if player1_name not in current_ladder:
                    write_user_feedback(f"{player1_name} doesn't exist!")
                    break
                if player2_name not in current_ladder:
                    write_user_feedback(f"{player2_name} doesn't exist!")
                    break
                
                # execute the query
                challenges_result = challenges_between_2_players(all_data, player1_name, player2_name)

                # draw the result of query
                draw_challenges(f"Challenges between {player1_name} and {player2_name}", challenges_result)

            elif key == "Challenges on specific date":
                target_date = screen.textinput("Challenges on specific date", "Please enter the date that you wish to view the challenges (DD-MM-YYYY)")
                if not target_date:
                    break
                target_date = target_date.strip()
                # checking if inputs are valid
                try:
                    datetime.strptime(target_date, "%d-%m-%Y")
                except ValueError:
                    write_user_feedback(f"{target_date} is an invalid date!")
                    break
                # execute the query
                challenges_result = challenges_on_specific_date(all_data, target_date)
                # draw the result of query
                draw_challenges(f"Challenges on {target_date}", challenges_result)

            elif key == "Challenges belonging to player":
                player_name = screen.textinput("Challenges belonging to player", "Please enter name of player that you wish to view the challenges:")
                # checking if inputs are valid
                if not player_name:
                    break
                player_name = player_name.strip()
                if player_name not in current_ladder:
                    write_user_feedback(f"{player_name} doesn't exist!")
                    break
                # execute the query
                challenges_result = challenges_belonging_to_player(all_data, player_name)
                # draw the result of query
                draw_challenges(f"Challenges belonging to {player_name}", challenges_result)

            elif key == "Most active player":
                # execute query
                player_name, challenges_result = most_active_player(all_data)
                # draw result of query
                draw_challenges(f"Most active player: {player_name}", challenges_result)

            elif key == "Least active player":
                # execute query
                player_name, challenges_result = least_active_player(all_data)
                # draw result of query
                draw_challenges(f"Least active player: {player_name}", challenges_result)

            elif key == "Challenges within date range":
                user_input = screen.textinput("Challenges within date range", "Please enter the date range that you wish to view the challenges, separated by a comma.\ne.g. '01-02-2021, 20-02-2021'")
                if not user_input:
                    break
                # checking if inputs are valid
                try:
                    start_date, end_date = [x.strip() for x in user_input.split(",")]
                except ValueError:
                    write_user_feedback("Incorrect input format!")
                    break
                try:
                    datetime.strptime(start_date, "%d-%m-%Y")
                except ValueError:
                    write_user_feedback(f"{start_date} is an invalid date!")
                    break
                try:
                    datetime.strptime(end_date, "%d-%m-%Y")
                except ValueError:
                    write_user_feedback(f"{end_date} is an invalid date!")
                    break
                # execute query
                challenges_result = challenges_within_date_range(all_data, start_date, end_date)
                # draw the results of query
                draw_challenges(f"Challenges between {start_date} and {end_date}", challenges_result)

            break

# draw the main screen first
draw()

# keep the window running
screen.mainloop()
