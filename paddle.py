from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.heading = 90

    def move_up(self):
        if self.ycor() < 260:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -260:
            self.sety(self.ycor() - 20)

    def change_heading(self, heading):
        self.heading = heading
