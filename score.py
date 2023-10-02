from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.left_score = 0
        self.right_score = 0
        self.score_write()

    def score_write(self):
        self.write(f"{self.left_score}    {self.right_score}", align="right", font=("Ariel", 30, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.score_write()

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.score_write()
