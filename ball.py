import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("slowest")
        self.sleep_time = 0.1
        self.penup()
        self.goto((-200, -200))
        self.x_move = 10
        self.y_move = 10

    def refresh(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_x(self):
        """when ball hits the side walls"""
        self.x_move *= -1

    def bounce_y(self):
        """when ball hits the bricks or top wall"""
        self.y_move *= -1

    def restart(self):
        self.goto(-200, -200)
        time.sleep(1)
        self.bounce_x()
        self.x_move = 10
        self.y_move = 10





