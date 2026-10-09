# for i in range(100):
#     print("We like Python's turtles!")
# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# for i in months:
#     print("One of the months of the year is", i)
# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for i in numbers:
#     print(i, "squared is", i*i)
import turtle
from cgi import print_environ_usage

wn = turtle.Screen()
t = turtle.Turtle()
# t.penup()
# t.goto(-200,0   )
# t.pendown()
# for i in range(3):
#     t.forward(80)
#     t.left(120)
#
#
# t.penup()
# t.forward(100)
# t.pendown()
#
#
# for i in range(4):
#     t.forward(80)
#     t.left(90)
#
# t.penup()
# t.forward(140)
# t.pendown()
#
#
# for i in range(6):
#     t.forward(80)
#     t.left(60)



t.pensize(3)
t.shape("turtle")
wn.bgcolor("pink")
t.color("white")

t.stamp()
t.penup()


for i in range(12):
    t.forward(125)
    t.pendown()
    t.forward(15)
    t.penup()
    t.forward(25)
    t.stamp()
    t.backward(165)
    t. left(30)









wn.exitonclick()