import colorgram
from turtle import Turtle, Screen, colormode, numinput
import random

colormode(255)

my_colors = colorgram.extract('ukiyo-e-woodblock-prints.jpg', 20)

ukiyo_colors = []
for color in my_colors:
    rgb = color.rgb
    rgb_tuple = (rgb.r, rgb.g, rgb.b)
    ukiyo_colors.append(rgb_tuple)

cursor = Turtle()
cursor.shape("circle")
cursor.shapesize(1, 1, 2)
cursor.color(38, 45, 47)
cursor.speed("fastest")
cursor.penup()


def create_painting(set_width_dots, set_height_dots, set_dot_size):
    painting_width_dots = set_width_dots
    painting_height_dots = set_height_dots
    dot_size = set_dot_size
    spacing = dot_size * 1.5

    my_screen = Screen()
    my_screen.title("Japanese Hirst")
    my_screen.bgcolor(32, 66, 71)
    screen_width = (painting_width_dots + 3) * spacing
    screen_height = (painting_height_dots + 3) * spacing
    my_screen.setup(screen_width, screen_height)

    move_back = -((screen_width / 2) - spacing)
    move_up = -((screen_height / 2) - (spacing * 2))
    for n in range(painting_height_dots):
        cursor.setpos(move_back, move_up)
        for _ in range(painting_width_dots):
            cursor.forward(spacing)
            pick_color = random.choice(ukiyo_colors)
            cursor.dot(dot_size, pick_color)
        move_up += spacing
    cursor.hideturtle()

    my_screen.exitonclick()


width = int(numinput("CreateHirstPainting", "Width in # dots: ", minval=1, maxval=20))
height = int(numinput("CreateHirstPainting", "Height in # dots: ", minval=1, maxval=20))
dots = int(numinput("CreateHirstPainting", "Dot size: ", minval=1, maxval=60))
create_painting(set_width_dots=width, set_height_dots=height, set_dot_size=dots)
