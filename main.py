from turtle import *
from random import randint

arr = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
for i in range(10000):
    t = Turtle()
    t.speed('fastest')
    t.shape('turtle')
    t.color(arr[randint(0, 5)])
    t.pensize(randint(20, 100))
    t.penup()
    t.goto(randint(-200, 200), randint(-200, 200))
    t.pendown()
    if randint(0, 1):
        t.left(randint(0, 360))
        t.forward(randint(0, 2000))
    else:
        t.begin_fill()
        t.circle(randint(0, 200))
        t.end_fill()
exitonclick()
