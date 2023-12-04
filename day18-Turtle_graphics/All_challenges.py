import turtle
from turtle import Turtle, Screen

"""
creating object timmy from the turtle class, changing the shape of the 
turtle-navigator to a turtle shape and making its color red
"""
timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")

"""
Turtle drawing a square
"""
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
"""
or
"""
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

"""
Turtle drawing different shapes, with random colors
"""
# from random import choice
#
# colours = ["red", "blue", "green", "purple", "yellow", "wheat", "SeaGreen", "IndianRed", "DeepSkyBlue"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.left(angle)
#
#
# for shape_side_n in range(3, 11):
#     timmy.color(choice(colours))
#     draw_shape(shape_side_n)


"""
Generate a random walk, with random colors from list - colours
"""
# from random import choice
#
# colours = ["red", "blue", "green", "purple", "yellow", "wheat", "SeaGreen", "IndianRed", "DeepSkyBlue"]
# direction = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")
#
# for _ in range(500):
#     timmy.color(choice(colours))
#     timmy.forward(30)
#     timmy.setheading(choice(direction))


"""How to generate random rgb colors"""
# from random import choice, randint
#
# turtle.colormode(255)
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     colour = (r, g, b)
#     return colour
#
# direction = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")
#
# for _ in range(500):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(choice(direction))

"""
Draw a Spirograph, with random rgb colors
"""
from random import randint

turtle.colormode(255)
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colour = (r, g, b)
    return colour

timmy.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)



"""
to show the screen, and making it only exit when clicked
"""
screen = Screen()
screen.exitonclick()
