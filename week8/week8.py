# def getgrade(mark):
#     if mark >= 90:
#         return "A"
#     elif mark>= 80:
#         return "B"
#     elif mark>= 70:
#         return "C"
#     elif mark>= 60:
#         return "D"
#     else:
#         return "F"
#
# marks = [95, 62, 23,69,34,97,66]
# for mark in marks:
#     print("your grade is", getgrade(mark))




# import turtle
#
#
#
#
# def choosecolor(height):
#     if height <=60:
#         return "red"
#     elif height <=70:
#         return "yellow"
#     else:
#         return "green"
#
#
#
#
#
#
#
# def drawbar(t, height, gap):
#     if height <=0:
#         labely = height + gap
#     else:
#         labely = gap
#     t.penup()
#     t.left(90)
#     t.forward(labely)
#     t.write("" + str(height))
#     t.backward(labely)
#     t.right(90)
#     t.pendown()
#     t.fillcolor(choosecolor(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
#
#
# def barchart(data):
#     maxheight = max(data)
#     num_bars = len(data)
#     min_height = min(data)
#     border = 10
#     bottom = min(min_height, 0)
#     gap = (maxheight + border) / 25
#
#
#     wn = turtle.Screen()
#     wn.bgcolor("white")
#     right = 40 * num_bars + border
#     top = maxheight + 4 * border
#     wn.setworldcoordinates(-border, bottom, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.fillcolor("red")
#     t.pensize(3)
#     t.speed(6)
#
#
#     for height in data:
#         drawbar(t, height, gap)
#     wn.exitonclick()
#
# data = [95, 62, -23, 69, 34, 97, -66]
# barchart(data)

def sqrt(x):
    return x ** 0.5
    print(int(input("Enter a number: ", x)))







import math

def findhypote(a,b):
    hypot = math.sqrt(a ** + b ** 2)
    return hypot

def withmath(a, b,):
    hypot = math.sqrt(a ** 2 + b ** 2)
    return hypot

print(withmath(3, 4))
print(findhypote(3, 4))



