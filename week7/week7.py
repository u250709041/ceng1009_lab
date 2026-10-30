# def sumto(n):
#     total = n * (n+1) / 2
#     return total
#
#
# print(sumto(10))
#
# n = int(input("enter a number"))
# print(int(sumto(n)))
# import turtle
#
#
# def drawstar(t, n, size):
#     angle = 180 - 180/2
#     for i in range(n):
#         t.right(angle)
#
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
#
# drawstar(t, 11, 4)



#
# def sumto(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#     return total
#
# print(sumto(10))
#
#
# n = int(input("enter a number:"))
# print(sumto(n))


# import math
#
#
# def mysqrt(x):
#     guess = x /2
#     for i in range(20):
#         guess = (1/2) * (guess + x / guess)
#     return (guess)
#
# n = int(input("enter a positive number"))
# print(mysqrt(n))
# print(math.sqrt(n))

# import turtle
#
# def drawsprite(someturtle, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
# def fancysquare(t, size):
#     for corner in range(4):
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# t = turtle.Turtle()
# t.pensize(2)
# t.color("hotpink")
#
#
#
# def drawtip(t, size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size / 2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size / 2)
#     t.right(90)
#     t.end_fill()
#
#
# def withtips(some, legs, length):
#     angle = 360 / legs
#     for i in range(legs):
#         some.forward(length)
#         drawtip(some, 10)
#         some.backward(length)
#         some.left(angle)
#
#
# def fancysquare(t, size):
#     for corner in range(4):
#         withtips(t, 8, 20)
#         t.forward(size)
#         t.left(90)
#
#
# wn = turtle.Screen()
# wn.bgcolor("black")
# t = turtle.Turtle()
# t.color("white")
# t.pensize(2)
# t.speed(0)
#
# fancysquare(t, 100)



# def check(n):
#     if n > 0:
#         return "positive"
#     elif n < 0:
#         return "negative"
#     else:
#         return "zero"
#
# num_list = (-7, 5, 0)
#
#
# for number in num_list:
#     print(check(number))
#
# n = int(input("enter a number:"))
# print(check(n))




import turtle




def drawbar(t, height, gap):
    t.penup()
    t.left(90)
    t.forward(height + gap)
    t.write("" + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown()


    t.begin_fill()
    t.left(90)
    t.forward(height)

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()



def barchart(data):
    maxheight = max(data)
    num_bars = len(data)


    border = 10
    gap = (maxheight + border) / 25


    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    right = 40 * num_bars + border
    top = maxheight + 4 * border
    wn.setworldcoordinates(-border, -border, right, top)

    t = turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(3)

    for height in data:
        drawbar(t, height, gap)


data = [48, 117, 200, 240, 160, 260, 220]
barchart(data)





wn.exitonclick()