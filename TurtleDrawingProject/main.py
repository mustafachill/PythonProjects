import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle Yapıyoruz")

turtle_instance = turtle.Turtle()
#turtle_instance_2 = turtle.Turtle()
'''
number_of_shade = 6
angle = 360 / number_of_shade
length = 60


for i in range(6):
    turtle_instance.left(angle)
    turtle_instance.forward(length)
'''
def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

turtle_instance.circle(100)

turtle.done()