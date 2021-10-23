from turtle import Turtle
import random
x = (-385, 380)
y = (-280, 285)


class Bat(Turtle):

    def __init__(self, position):
        super().__init__()

        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.shape("square")
        self.color("white")
        self.goto(position)
        self.setheading(90)

    def move_up(self):
        if self.heading() != 90:
            self.setheading(90)
        if self.ycor() <= 245:
            self.forward(30)

    def move_down(self):
        if self.heading != 270:
            self.setheading(270)
        if self.ycor() >= -245:
            self.forward(30)



class Net(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.pensize(5)
        self.color("white")
        self.make_dash()

    def make_dash(self):
        for _ in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
