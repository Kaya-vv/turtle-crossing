from turtle import Turtle
import random
import time

AMOUNT_OF_CARS = 20


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


class Cars:
    def __init__(self):
        self.cars_list = []
        self.min_speed = 5
        self.max_speed = 10

    def create_cars(self):

        for _ in range(AMOUNT_OF_CARS):
            car = Turtle("square")
            car.penup()
            random_y = random.randint(-240, 260)
            random_x = random.randint(-280, 280)
            car.goto((random_x, random_y))
            car.color(random_color())
            car.shapesize(1, 2)
            self.cars_list.append(car)

    def move_cars(self):

        for car in self.cars_list:
            car_speed = random.randint(self.min_speed, self.max_speed)
            random_y = random.randint(-240, 260)
            car.backward(car_speed)
            if car.xcor() < -320:
                car.color(random_color())
                car.goto(320, random_y)

    def increase_speed(self):
        self.min_speed += 3
        self.max_speed += 3
