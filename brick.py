from turtle import Turtle
import random
COLORS = ["blue", "yellow", "orange", "pink", "green", "cyan", "gold", "red"]


class Brick(Turtle):
    def __init__(self, position, length):
        super().__init__()
        self.shape("square")
        self.color(f"{random.choice(COLORS)}")
        self.shapesize(stretch_wid=2, stretch_len=length)
        self.penup()
        self.goto(position)

