from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.colormode(255)

player = Player()
car = Cars()
scoreboard = Scoreboard()
car.create_cars()
screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    car.move_cars()

    # If player levels up
    if player.ycor() > 280:
        player.reset_pos()
        car.increase_speed()
        scoreboard.update_score()

    # If player collides with car
    for single in car.cars_list:
        if player.distance(single) < 24:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
