from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        x_cor = self.xcor() + self.x
        y_cor = self.ycor() + self.y
        self.goto(x_cor, y_cor)

    def bounce_ycor(self):
        self.y *= -1

    def bounce_xcor(self):
        self.x *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_xcor()
