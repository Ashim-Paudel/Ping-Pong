from turtle import Turtle


class ScoreKeeper(Turtle):

    def __init__(self, position):
        super().__init__()

        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(position)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(arg=f"{self.score}", align="center", font=('Aerial', 24, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()
