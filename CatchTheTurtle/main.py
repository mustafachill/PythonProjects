import turtle
import random
from tkinter import *
'''
# Zaman ile fonksiyon çağırma
https://www.geeksforgeeks.org/turtle-ontimer-function-in-python/
'''
# screen
turtle_table = turtle.Screen()
turtle_table.bgcolor("lightpink")
grid_size = 20
x_grid = 10
y_grid = 10
score = 0
time = 60
game_over = False
# writing turtles
FONT = ("Arial",30,"normal")
top_height = 350
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("dark blue")
score_turtle.penup()
score_turtle.setpos(0,top_height)
score_turtle.write(f"Score : {score}",False,"center",font=FONT)

#turtle list
turtle_list = []

def make_turtle(grid_size,x,y):
    # instance turtle
    turtle_instance = turtle.Turtle()
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score : {score}", False, "center", font=FONT)
        #print(x,y)

    turtle_instance.onclick(handle_click)
    turtle_instance.shape("turtle")
    turtle_instance.color("dark green")
    turtle_instance.shapesize(3)
    turtle_instance.penup()
    turtle_instance.goto(x * grid_size, y * grid_size)
    turtle_list.append(turtle_instance)

def setup_turtle():

    x = x_grid
    y = y_grid
    for i in range(4):
        for j in range(5):
            make_turtle(grid_size, x, y)
            x -= 5
        x = x_grid
        y -= 5


def hide_turtle():
    for turtle_ in turtle_list:
        turtle_.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        turtle.ontimer(show_turtles_randomly,500)
    else:
        hide_turtle()
def countdown(time):
    global game_over
    countdown_turtle = turtle.Turtle()
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()
    countdown_turtle.setpos(0, top_height - 50)
    if time > 0:
        countdown_turtle.write(f"Time : {time}", False, "center", font=FONT)
        turtle.ontimer(countdown_turtle.clear, 1000)
        turtle.ontimer(lambda : countdown(time - 1),1000)
    else:
        countdown_turtle.clear()
        countdown_turtle.write(f"Time is over!", False, "center", font=FONT)
        game_over = True


def start_game():
    turtle.tracer(0)
    setup_turtle()
    hide_turtle()
    countdown(10)
    show_turtles_randomly()
    turtle.tracer(1)

start_game()


turtle.done()