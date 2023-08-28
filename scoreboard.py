from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(f"{self.score}", font=('Arial', 30, 'normal'))

    def count_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", font=('Arial', 30, 'normal'))

    def game_over(self):
        self.goto(15, 0)
        self.write("Game Over", font=('Arial', 50, 'normal'), align="center")
