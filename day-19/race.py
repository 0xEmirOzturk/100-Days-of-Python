import turtle
from turtle import Turtle, Screen
import random

race = False

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_pos = [-70, -40, -10, 20, 50, 80]

all_turtles = []



for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.speed(10)
    tim.penup()
    tim.goto(x=-230, y=y_pos[i])
    all_turtles.append(tim)


if user_bet:
    race = True

while race:

    for turtles in all_turtles:
        if turtles.xcor() > 230:
            race = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You\'ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"You\'ve lost! The {winning_color} turtle is the winner!")

        turtles.forward(random.randint(0, 10))

screen.exitonclick()