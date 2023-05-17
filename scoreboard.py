from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.score = 0
        # calling the scoreboard during initialization
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 200)
        self.write(f"BREAK OUT               Score: {self.score}", align="center", font=("Courier", 40, "normal"))

    def update_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

