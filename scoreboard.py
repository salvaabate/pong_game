from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.l_score}         {self.r_score}", align=ALIGN, font=FONT)

    def add_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def add_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def is_game_over(self):
        if self.l_score == 10 or self.r_score == 10:
            return True
        return False
