from turtle import Turtle

RANDOMIZER = [-1, 1]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if abs(self.ycor()) >= 280:
            self.bounce(True)

    def bounce(self, wall):
        if wall:
            self.y_move *= -1
        else:
            self.x_move *= -1
            self.move_speed *= .5

    def restart(self):
        self.home()
        self.move_speed = 0.1
