from turtle import Turtle
import random
x = (-385, 380)
y = (-280, 285)


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("circle")
        self.color("white")
        self.pace_x = 10
        self.pace_y = 10

    def move(self):
        new_x = self.xcor()+self.pace_x
        new_y = self.ycor()+self.pace_y
        self.goto(new_x, new_y)

    def wall_collide(self):
        return self.ycor() >= 285 or self.ycor() <= -280

    def bat_collision(self, bat):
        return self.distance(bat) < 60

    def bounce_wall(self):
        self.pace_y *= -1

    def bounce_bat(self):
        self.pace_x *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.pace_x *= -1
        self.pace_y *= -1



