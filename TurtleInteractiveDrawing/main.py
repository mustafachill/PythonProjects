import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)
def turtle_backward():
    turtle_instance.backward(100)
def rotate_angle_right():
    turtle_instance.right(90)
def rotate_angle_left():
    turtle_instance.left(90)

def clear_screen():
    turtle_instance.clear()
def turtle_return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(turtle_forward,"Up")
drawing_board.onkey(turtle_backward,"Down")
drawing_board.onkey(rotate_angle_right,"Right")
drawing_board.onkey(rotate_angle_left,"Left")
drawing_board.onkey(clear_screen,"c")
drawing_board.onkey(turtle_return_home,"h")
drawing_board.onkey(turtle_pen_up,"w")
drawing_board.onkey(turtle_pen_down,"e")
turtle.done()