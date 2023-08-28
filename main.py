from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from line import Line
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

right = Paddle((370, 0))
left = Paddle((-380, 0))

ball = Ball()

line = Line()

r_score = ScoreBoard((150, 250))
l_score = ScoreBoard((-150, 250))

screen.onkeypress(right.move_up, "Up")
screen.onkeypress(right.move_down, "Down")
screen.onkeypress(left.move_up, "w")
screen.onkeypress(left.move_down, "s")

game = True
while game:
    time.sleep(ball.speed_ball)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right) < 55 and ball.xcor() > 340:
        ball.bounce_x()
        ball.add_speed()
    elif ball.distance(left) < 55 and ball.xcor() < -350:
        ball.bounce_x()
        ball.add_speed()

    if ball.xcor() > 380:
        l_score.count_score()
        ball.reset_ball()
    elif ball.xcor() < -390:
        r_score.count_score()
        ball.reset_ball()

    if r_score.score == 5:
        game = False
        r_score.game_over()
    elif l_score.score == 5:
        game = False
        l_score.game_over()


screen.exitonclick()
