from turtle import Turtle
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 270)
        self.color("black")
        self.write(f"Level: {self.level}",font=FONT,)

    def increase_score(self):
        self.level += 1

    def update_score(self):
        self.increase_score()
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, )

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
