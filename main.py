# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong Game")
screen.tracer(0)

x,y = 10,10

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball(x, y)
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #detecting collision
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bouncey()

    if ball.xcor() >320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bouncex()

    if ball.xcor() > 380:
        ball.resetme()
        score.score("l")

    if ball.xcor() < -380:
        ball.resetme()
        score.score("r")

screen.exitonclick()