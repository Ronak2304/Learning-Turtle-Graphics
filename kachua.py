from turtle import Turtle,Screen,colormode

tidda = Turtle()
# tidda.shape("turtle")
tidda.color("blue")
# tidda.pensize(15)
colormode(255)
tidda.speed(100)

# tidda.pencolor((202, 165, 0))
# tidda.forward(100)/
my_screen = Screen()
my_screen.bgcolor("orange")

# tidda.left(90)
# tidda.forward(100)
# tidda.right(90)

#decagon
# for i in range(10):
#     tidda.forward(85)
#     tidda.right(36)
#     tidda.pencolor("yellow")

# #nonagon
# for i in range(9):
#     tidda.forward(85)
#     tidda.right(40)
#     tidda.pencolor("blue")

# # #Octagon
# for i in range(8):
#     tidda.forward(85)
#     tidda.right(45)
#     tidda.pencolor("green")

# # heptagon
# for i in range(7):
#     tidda.forward(85)
#     tidda.right(51.42857142857143)
#     tidda.pencolor("red")

# # #hexagon
# for i in range(6):
#     tidda.forward(85)
#     tidda.right(60)
#     tidda.pencolor("khaki")

# # #Pentagon
# for i in range(5):
#     tidda.forward(85)
#     tidda.right(72)
#     tidda.pencolor("white")

# #Square
# for i in range(4):
#     tidda.forward(85)
#     tidda.right(90)
#     tidda.pencolor("coral")

# #triangle
# for i in range(3):
#     tidda.forward(85)
#     tidda.right(120)
#     tidda.pencolor("pink")


# for i in range(100):
#     if tidda.isvisible():
#         tidda.forward(i)
#         if i%2==0:
#             tidda.pencolor("blue")
#         else:    
#             tidda.pencolor("yellow")
#         if i%10==0:
#             tidda.circle(10)
#     else:
#         tidda.reset()
# tidda.circle(100)

# Random Walk
import random

def random_color_generator():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    ans = (r,g,b)
    return ans

# print(type(random_color_generator))
# def random_walk():
#     # tidda.speed(100)
#     rang = ['light blue', 'gold', 'light coral', 'red', 'indigo', 'dim gray', 'cyan', 
#         'peach puff','aqua', 'yellow', 'white', 'magenta', 'tan', 
#         'olive drab', 'dark green', 'teal', 'purple', 'lime', 'blue', 'hot pink', 
#         'steel blue', 'navy', 'forest green', 'saddle brown', 'green', 'goldenrod', 
#         'light green', 'lavender', 'turquoise', 'lime green', 'brown', 'khaki', 
#         'orange', 'dark gray', 'olive', 'orange red', 'deep sky blue', 'dark orange', 
#         'light pink', 'gray', 'dark red', 'black'
#     ]
#     def funx(x,y):
#         my_screen.bye()
        
#     my_screen.onclick(funx)
    
#     isTrue = True
#     while isTrue:
#         num = random.randint(1,3)
#         # rand_color = random.choice(rang)
#         if num==1:
#             tidda.left(90)
#         elif num==2:
#             tidda.left(90)
#             tidda.left(90)
#         elif num==3:
#             tidda.right(90)

#         colors = random_color_generator()
#         # print(colors)
#         tidda.pencolor(colors)
#         tidda.forward(38)
        
# random_walk()


# SpiroGraph Generator 
# for i in range(360):
#     tidda.setheading(i) #also tidda.left(i) can also be used 
#     tidda.circle(100)
#     tidda.pencolor(random_color_generator())




my_screen.exitonclick()