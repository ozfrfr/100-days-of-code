import colorgram
import turtle as t
import random

timmy = t

colors = colorgram.extract("Damien_Hirst.jpg", 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# gotten from rgb_colors[]
color_list = [(248, 247, 247), (243, 247, 246), (246, 243, 245), (239, 242, 245), (2, 13, 30), (45, 25, 18),
              (210, 134, 117), (16, 107, 159), (242, 210, 93), (221, 85, 68), (167, 5, 25), (166, 55, 89),
              (146, 79, 58), (185, 134, 154), (207, 71, 103), (97, 3, 16), (162, 162, 61), (9, 63, 35), (7, 97, 63),
              (32, 138, 75), (6, 210, 202), (6, 61, 138), (3, 171, 211), (140, 227, 216), (122, 190, 155),
              (124, 174, 191), (222, 177, 210), (97, 219, 227), (88, 54, 45), (32, 84, 90)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()

