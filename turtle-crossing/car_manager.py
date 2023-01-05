import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
STARTING_CARS_COUNT = 10
MOVE_INCREMENT = 10
CARS_COUNT_INCREMENT = 2


class CarManager:

    def __init__(self):
        self.cars = []
        self.level = 1
        self.car_move_distance = STARTING_MOVE_DISTANCE
        self.cars_count = STARTING_CARS_COUNT
        self.init_cars()

    def init_cars(self):
        for i in range(self.cars_count):
            car = self.add_new_car(random.choice(COLORS))
            car.forward(random.randint(10, 500))

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_move_distance)

    def recycle_cars(self):
        for car in self.cars:
            if car.xcor() < -310:
                self.add_new_car(car.pencolor())
                car.hideturtle()
                self.cars.remove(car)

    def next_level(self):
        for car in self.cars:
            car.hideturtle()
            self.cars.remove(car)

        self.cars_count += CARS_COUNT_INCREMENT
        self.car_move_distance + - MOVE_INCREMENT
        self.init_cars()

    def add_new_car(self, color):
        car = Turtle()
        car.penup()
        car.color(color)
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(300, random.randint(-255, 265))
        self.cars.append(car)
        return car
