from turtle import Turtle

STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)

    def reset_pos(self):
        self.goto(STARTING_POSITION)
