from turtle import Screen
from paddle import Paddle
from brick import Brick
from ball import Ball
from scoreboard import ScoreBoard
import time

# setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.tracer(0)

paddle = Paddle()

# move paddle right & left
screen.listen()
screen.onkey(key="Right", fun=paddle.go_right)
screen.onkey(key="Left", fun=paddle.go_left)

# setting up the bricks
bricks = []


def bricks_arrange():
    xcor_odd = -455
    xcor_even = -460
    for i in range(11):
        # arranging odd rows
        bricks.append(Brick((xcor_odd, -10), 4))
        bricks.append(Brick((xcor_odd, 80), 4))
        bricks.append(Brick((xcor_odd, 170), 4))
        xcor_odd += 90

    for i in range(14):
        # arranging even rows
        bricks.append(Brick((xcor_even, 35), 3))
        bricks.append(Brick((xcor_even, 125), 3))
        xcor_even += 70


bricks_arrange()
# Ball
ball = Ball()
# score
score = ScoreBoard()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.sleep_time)
    ball.refresh()  # ball's position keeps updating on every iteration

    # collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 40:
            ball.bounce_y()
            # remove the brick
            bricks.remove(brick)
            brick.hideturtle()
            score.update_point()

    # collision with the top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # collision with the side walls
    if ball.xcor() < -470 or ball.xcor() > 470:
        ball.bounce_x()

    # collision with the paddle
    if ball.distance(paddle) < 40 and ball.ycor() < -250:
        ball.bounce_y()
        ball.sleep_time *= 0.98
        if ball.sleep_time < 0:
            ball.sleep_time = 0

    # paddle misses ball
    if ball.ycor() < -270:
        ball.restart()
        score.clear()
        score.score = 0
        score.update_scoreboard()
        paddle.goto(0, -270)
        bricks_arrange()
        ball.sleep_time = 0.1


screen.exitonclick()
