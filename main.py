import turtle

# Game settings
choices = ["Group 1's Rock, Paper & Scissors Game"]
player1_score = 0
player2_score = 0
round_count = 1
player1_input = ""
player2_input = ""

# Setup screen
screen = turtle.Screen()
screen.title("Group 1's Rock, Paper & Scissors Game")
screen.bgcolor("light blue")
screen.setup(800,600)
screen.register_shape('rock.gif')
screen.register_shape('paper.gif')
screen.register_shape('scissors.gif')

# Setup text writer
text_writer = turtle.Turtle()
text_writer.color("black")
text_writer.speed(0)
text_writer.penup()
text_writer.goto(-150, 270)
text_writer.write("Group 1's Rock, Paper & Scissors Game", font=50)
text_writer.goto(-200, 240)
text_writer.write("Player 1: Press 'A' for Rock, 'S' for Paper, and 'D' for Scissors",font=50)
text_writer.goto(-200, 210)
text_writer.write("Player 2: Press '4' for Rock, '5' for Paper, and '6' for Scissors",font=50)

text_writer.goto(-200, -250)
text_writer.write("\t          Group Member's:\n Lorem Ipsumm \t\t Lorem Ipsumm\n Lorem Ipsumm \t\t Lorem Ipsumm\n Lorem Ipsumm", font=50)

# Setup score writer
score_writer = turtle.Turtle()
score_writer.color("black")
score_writer.speed(0)
score_writer.penup()
score_writer.goto(-310, 100)
score_writer.write("Player 1's Score = {} \t\t\t\t     Player 2's Score = {}\n \t\t\tRound Count = {}".format(player1_score, player2_score, round_count), font=50)

# Setup player images
player1_image = turtle.Turtle()
player1_image.penup()
player1_image.speed(5)

player2_image = turtle.Turtle()
player2_image.penup()
player2_image.speed(5)

# Player choices
def choose(choice, player):
    global player1_input, player2_input
    if player == 1:
        player1_input = choice
    else:
        player2_input = choice
    check_round()

# Reset game
def reset_game():
    global player1_score, player2_score, round_count
    player1_score = 0
    player2_score = 0
    round_count = 1
    score_writer.clear()
    score_writer.write("Player 1's Score = {} \t\t\t\t     Player 2's Score = {}\n \t\t\tRound Count = {}".format(player1_score, player2_score, round_count), font=50)
    text_writer.clear()
    text_writer.goto(-150, 270)
    text_writer.write("Group 1's Rock, Paper & Scissors Game", font=50)
    text_writer.goto(-200, 240)
    text_writer.write("Player 1: Press 'A' for Rock, 'S' for Paper, and 'D' for Scissors",font=50)
    text_writer.goto(-200, 210)
    text_writer.write("Player 2: Press '4' for Rock, '5' for Paper, and '6' for Scissors",font=50)
    text_writer.goto(-200, -250)
    text_writer.write("\t          Group Member's:\n Lorem Ipsumm \t\t Lorem Ipsumm\n Lorem Ipsumm \t\t Lorem Ipsumm\n Lorem Ipsumm", font=50)
    screen.onkey(lambda: choose("Rock", 1), "a")
    screen.onkey(lambda: choose("Paper", 1), "s")
    screen.onkey(lambda: choose("Scissors", 1), "d")
    screen.onkey(lambda: choose("Rock", 2), "4")
    screen.onkey(lambda: choose("Paper", 2), "5")
    screen.onkey(lambda: choose("Scissors", 2), "6")

# Check round
def check_round():
    global player1_input, player2_input, round_count, player1_score, player2_score
    if player1_input and player2_input:  # if both players have made a move
        player1_image.goto(-250, -50)
        player2_image.goto(250, -50)
        player1_image.shape(player1_input.lower() + '.gif')
        player2_image.shape(player2_input.lower() + '.gif')
        if player1_input == player2_input:
            pass  # no change in score
        elif (player1_input == "Rock" and player2_input == "Scissors") or (player1_input == "Paper" and player2_input == "Rock") or (player1_input == "Scissors" and player2_input == "Paper"):
            player1_score += 5
        else:
            player2_score += 5
        score_writer.clear()
        score_writer.write("Player 1's Score = {} \t\t\t\t     Player 2's Score = {}\n \t\t\t   Round Count = {}".format(player1_score, player2_score, round_count), font=50)
        player1_input = ""
        player2_input = ""
        round_count += 1  # increment round_count by 1 every time an image is thrown

        if player1_score >= 50 or player2_score >= 50:
            winner = "Player 1" if player1_score >= 50 else "Player 2"
            text_writer.goto(-100,0)
            text_writer.write("Game Over! {} wins!\n       Press R to reset".format(winner), font=50)
            screen.onkey(None, "a")
            screen.onkey(None, "s")
            screen.onkey(None, "d")
            screen.onkey(None, "4")
            screen.onkey(None, "5")
            screen.onkey(None, "6")


# Listen for key presses
screen.listen()
screen.onkey(lambda: choose("Rock", 1), "a")
screen.onkey(lambda: choose("Paper", 1), "s")
screen.onkey(lambda: choose("Scissors", 1), "d")
screen.onkey(lambda: choose("Rock", 2), "4")
screen.onkey(lambda: choose("Paper", 2), "5")
screen.onkey(lambda: choose("Scissors", 2), "6")
screen.onkey(reset_game, "r")

# Main game loop
while True:
    screen.update()
