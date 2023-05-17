from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.speed("fastest")
        self.penup()
        self.goto((0, -270))

    def go_left(self):
        if self.xcor() < -380:
            pass
        else:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() > 380:
            pass
        else:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
