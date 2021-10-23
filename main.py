"""the classic pong game"""
from turtle import Turtle, Screen
from ball import Ball
from bat import Bat, Net
from score_tracker import ScoreKeeper
import random, time

SPEED = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
bat_right = Bat((384, 0))
bat_left = Bat((-390, 0))
net = Net()

r_player = ScoreKeeper((50, 250))
l_player = ScoreKeeper((-50, 250))
screen.update()

screen.listen()
screen.onkeypress(fun=bat_right.move_up, key="Up")
screen.onkeypress(fun=bat_right.move_down, key="Down")
screen.onkeypress(fun=bat_left.move_up, key="w")
screen.onkeypress(fun=bat_left.move_down, key="s")

game_on = True
while game_on:
    screen.update()
    time.sleep(SPEED)

    ball.move()
    if ball.wall_collide():
        ball.bounce_wall()

    if ball.bat_collision(bat_right) and ball.xcor() >= 365:
        ball.bounce_bat()
        SPEED *= 0.83

    if ball.bat_collision(bat_left) and ball.xcor() <= -380:
        ball.bounce_bat()
        SPEED *= 0.83

    if ball.xcor() >= 400 and not ball.bat_collision(bat_right):
        l_player.increase_score()
        ball.ball_reset()
        SPEED = 0.1

    if ball.xcor() <= -400 and not ball.bat_collision(bat_left):
        r_player.increase_score()
        ball.ball_reset()
        SPEED = 0.1

screen.exitonclick()