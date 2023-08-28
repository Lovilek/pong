from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.color("white")

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)
