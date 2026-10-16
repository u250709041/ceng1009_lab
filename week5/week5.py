# import random
#
#
# for i in range(10):
#     print(random.random())



# import random

# for i in range(10):
#     print(random.randint(25, 35))



# import math
#
# a = int(input("enter a :"))
# b = int(input("emter b :"))
# c = math.hypot(a, b)
# # c = math.sqrt(a**2 + b**2)
# print(c)

#
# import math
#
# def areaofcircle(r):
#     area = math.pi * r**2
#     return area
# print(areaofcircle(5))
#     # return masth.pi * r**2



# import turtle
#
# def drawStar(t, side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# drawStar(tess, 200)
#
# screen.exitonclick()

import turtle
a = turtle.Turtle()
wn = turtle.Screen()
def drawsquare(a, side):
    for i in range(4):
        a.forward(side)
        a.left(90)
#
wn.bgcolor("pink")
a.color("white")
a.pensize(3)
a.speed(0)
#
# for i in range(5):
#     drawsquare(a, 20)
#     a.penup()
#     a.forward(40)
#     a.pendown()


for i in range(20, 121, 20):
    drawsquare(a, i)
    a.penup()
    a.backward(10)
    a.right(90)
    a.forward(10)
    a.left(90)
    a.pendown()

























wn.exitonclick()