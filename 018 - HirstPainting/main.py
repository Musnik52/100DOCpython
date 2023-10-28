# from turtle import Turtle, Screen, colormode
# import random

# colormode(255)
# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("magenta")
# colors = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]


# def rand_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# # #square:
# # for i in range(4):
# #     turtle.forward(100)
# #     turtle.right(90)

# # #dashed line:
# # for i in range (10):
# #     turtle.forward(8)
# #     turtle.penup()
# #     turtle.forward(8)
# #     turtle.pendown()

# # # many shapes / fractal:
# # for i in range(3, 11):
# #     turtle.color(random.choice(colors))
# #     for j in range(i):
# #         turtle.forward(60)
# #         turtle.right(360 / i)

# # # random walk:
# # turtle.speed("fastest")
# # turtle.width(7)
# # directions = [0, 90, 180, 270]
# # for i in range(100):
# #     turtle.color(rand_color())
# #     turtle.forward(30)
# #     turtle.setheading(random.choice(directions))


# # # spirograph:
# # def draw_spirograph(gap_size):
# #     turtle.speed("fastest")
# #     for i in range(int(360 / gap_size)):
# #         turtle.color(rand_color())
# #         turtle.circle(100)
# #         turtle.setheading(turtle.heading() + gap_size)


# # draw_spirograph(10)


# screen = Screen()
# screen.exitonclick()

# PAINTING:
# Extracting the color RGB list:
# import colorgram

# colors = colorgram.extract("018 - HirstPainting/image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))


# print(rgb_colors)
# # [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

from turtle import Turtle, Screen, colormode
import random

colormode(255)
turtle = Turtle()
turtle.hideturtle()
turtle.color("magenta")
turtle.speed("fastest")

color_list = [
    (198, 13, 32),
    (248, 236, 25),
    (40, 76, 188),
    (244, 247, 253),
    (39, 216, 69),
    (238, 227, 5),
    (227, 159, 49),
    (29, 40, 154),
    (212, 76, 15),
    (17, 153, 17),
    (241, 36, 161),
    (195, 16, 12),
    (223, 21, 120),
    (68, 10, 31),
    (61, 15, 8),
    (223, 141, 206),
    (11, 97, 62),
    (219, 159, 11),
    (54, 209, 229),
    (19, 21, 49),
    (238, 157, 216),
    (79, 74, 212),
    (10, 228, 238),
    (73, 212, 168),
    (93, 233, 198),
    (65, 231, 239),
    (217, 88, 51),
]

turtle.up()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
dots_ammount = 100

for dot_count in range(1, dots_ammount + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = Screen()
screen.exitonclick()
