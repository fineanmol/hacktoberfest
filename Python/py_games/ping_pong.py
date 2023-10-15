import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("gray")
wn.setup(width=800, height=600)

# Score
score_player = 0
score_computer = 0

# Paddle Player
paddle_player = turtle.Turtle()
paddle_player.speed(0)
paddle_player.shape("square")
paddle_player.color("black")
paddle_player.shapesize(stretch_wid=5, stretch_len=1)
paddle_player.penup()
paddle_player.goto(-350, 0)

# Paddle Computer
paddle_computer = turtle.Turtle()
paddle_computer.speed(0)
paddle_computer.shape("square")
paddle_computer.color("black")
paddle_computer.shapesize(stretch_wid=5, stretch_len=1)
paddle_computer.penup()
paddle_computer.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player: 0  Computer: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_player_up():
    y = paddle_player.ycor()
    y += 20
    paddle_player.sety(y)

def paddle_player_down():
    y = paddle_player.ycor()
    y -= 20
    paddle_player.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_player_up, "w")
wn.onkeypress(paddle_player_down, "s")

# Main game loop
while True:
    wn.update()

    # Move the computer paddle
    if ball.dx > 0 and paddle_computer.ycor() < ball.ycor():
        paddle_computer.sety(paddle_computer.ycor() + 1)

    if ball.dx > 0 and paddle_computer.ycor() > ball.ycor():
        paddle_computer.sety(paddle_computer.ycor() - 1)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_player += 1
        pen.clear()
        pen.write("Player: {}  Computer: {}".format(score_player, score_computer), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_computer += 1
        pen.clear()
        pen.write("Player: {}  Computer: {}".format(score_player, score_computer), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_computer.ycor() + 50 > ball.ycor() > paddle_computer.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_player.ycor() + 50 > ball.ycor() > paddle_player.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
