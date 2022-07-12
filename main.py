import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


def make_net():
    net = Turtle()
    net.color("white")
    net.hideturtle()
    net.penup()
    net.goto(0, -300)
    net.seth(90)
    net.pensize(5)
    intervals = screen.canvheight / 15
    for i in range(15):
        net.pendown()
        net.forward(intervals)
        net.penup()
        net.forward(intervals)


def hit_paddle(paddle):
    if abs(ball.xcor()) > 320 and ball.distance(paddle) < 50:
        return True
    return False


def hit_edge():
    if ball.xcor() >= 380:
        scoreboard.add_l_score()
        ball.restart()
        screen.update()
    elif ball.xcor() <= -380:
        scoreboard.add_r_score()
        ball.restart()
        screen.update()


make_net()
screen.listen()
scoreboard = Scoreboard()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
ball = Ball()

game_end = False

while not game_end:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # check if ball bounced off a paddle
    if hit_paddle(left_paddle):
        ball.bounce(False)
    elif hit_paddle(right_paddle):
        ball.bounce(False)

    hit_edge()

    if scoreboard.is_game_over():
        scoreboard.game_over()
        game_end = True

screen.exitonclick()
