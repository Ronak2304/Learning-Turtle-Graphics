###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

# rgb_colors = []
# colors = colorgram.extract('LearningTurtleGraphics\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
(170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

from turtle import Turtle,Screen,colormode
import random 

"""
Generating hirst Painting
painting should be of 10rows x 10columns size 
dot size - 20, space 50

"""


def random_color_generate(colour_list):
    rand_index = random.randint(0,26)
    ans =  colour_list[rand_index]
    return ans

colormode(255)
oggy = Turtle()
oggy.penup() 
oggy.backward(200)
oggy.right(90)
oggy.forward(200)
oggy.left(90)
x = oggy.xcor()
y = oggy.ycor()
for i in range(0,10):
    for i in range(0,10):
        oggy.dot(20,random_color_generate(color_list))
        oggy.forward(50)
    oggy.setx(x)
    oggy.sety(y)
    oggy.left(90)
    oggy.forward(50)
    x = oggy.xcor()
    y = oggy.ycor()
    oggy.right(90)

my_screen = Screen()
my_screen.exitonclick()

