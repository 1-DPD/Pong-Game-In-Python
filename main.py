import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game Using Python")
screen.tracer(0)

ball = Ball()
score = Score()

right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))


screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "u")
screen.onkey(left_paddle.down, "d")


continue_game = True
while continue_game:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_ycor()

    if ball.distance(right_paddle) < 30 and ball.xcor() > 320 or ball.distance(left_paddle) < 30 and ball.xcor() < -320:
        ball.bounce_xcor()

    if ball.xcor() > 380:
        ball.reset()
        score.increase_left_score()
        score.score_write()

    if ball.xcor() < -380:
        ball.reset()
        score.increase_right_score()
        score.score_write()

screen.exitonclick()
