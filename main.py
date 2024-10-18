# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 18 - Intermediate - Project - Hirst Spot Painting Using Python Turtle Package
import turtle as turtle_module
import random

# # Below code needs to be ran once to extract colors for an image
# import colorgram
#
# # Extract 35 colors from an image.
# colors_object = colorgram.extract('hirst-spot-painting.jpg', 35)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors_object[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# # hsl = first_color.hsl # e.g. (230, 255, 203)
#
# # print(colors_object) # checking
# # print(first_color) # checking
# # print(rgb) # checking
# # print(rgb[0]) # checking
#
# def make_colors_list(colors_colorgram):
#     """Takes colors object from colorgram.py libray and returns an RGB list of tuples."""
#     colors_list = []
#     for color in colors_colorgram:
#         # color_rgb = color.rgb[0]
#         rgb_list = [] # this list collects values for a single color
#         for n in range(0,3):
#             rgb_list.append(color.rgb[n])
#         rgb_tuple = tuple(rgb_list)
#         colors_list.append(rgb_tuple)
#     return colors_list
#
# new_colors = make_colors_list(colors_object)
# print(new_colors)

# Manually removed colors that are too close to white
colors = [(135, 164, 199), (223, 151, 105), (31, 43, 62), (200, 137, 148), (160, 61, 51), (235, 212, 94), (50, 100, 139), (138, 181, 162), (147, 64, 72), (56, 49, 46), (160, 32, 29), (61, 115, 99), (228, 165, 171), (168, 29, 33), (52, 40, 44), (209, 86, 76), (236, 166, 157), (34, 60, 54), (15, 96, 70), (35, 59, 104), (173, 187, 218), (192, 100, 108), (107, 126, 158), (174, 201, 191), (37, 149, 205), (20, 82, 103), (64, 66, 57), (157, 202, 220), (100, 142, 131), (129, 130, 123)]
print(len(colors)) # 30 colors left

# Create a 10x10 painting of random color dots using turtle, each dot ~20, space of 50
timmy = turtle_module.Turtle()
timmy.shape("turtle")
timmy.speed("slow") # values of slowest, slow, normal, fast and fastest
turtle_module.colormode(255) # set the RGB color mode to 0 - 255 range

# Start at bottom left corner of the painting
x_pos = -250
y_pos = -250

# Make a million $ Hirst spot painting using a turtle:
# timmy.hideturtle()
timmy.penup()
for y in range(0, 10):
    for x in range(0, 10):
        random_color = random.choice(colors)
        timmy.setpos(x_pos, y_pos)
        timmy.dot(20, random_color)
        x_pos += 50
    x_pos = -250
    y_pos += 50
x_pos = -250
timmy.setpos(x_pos, y_pos)

# Create a window, should be at the bottom
screen = turtle_module.Screen()
screen.exitonclick()