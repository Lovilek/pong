from turtle import Turtle


class Line:
    def __init__(self):
        coordinate = 0
        for i in range(0, 8):
            block = Turtle()
            block.penup()
            block.color("white")
            block.shape("square")
            block.shapesize(stretch_wid=0.5, stretch_len=0.5)
            block.goto(x=0, y=coordinate)
            coordinate += 40

        coordinate = 0
        for i in range(0, 8):
            block = Turtle()
            block.penup()
            block.color("white")
            block.shape("square")
            block.shapesize(stretch_wid=0.5, stretch_len=0.5)
            block.goto(x=0, y=coordinate)
            coordinate -= 40
