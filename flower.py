from turtle import *
from colorsys import hsv_to_rgb

bgcolor("black")
speed(0)

pensize(9)
pencolor("white")

pendown()
c = 0
for i in range(50):
    c += 1/50
    for j in range(4):
        color(hsv_to_rgb(c, j/4, 0.8))
        right(90)
        circle(200-j*4, 90)
        left(90)
        circle(200-j*4, 90)
        right(180)
        circle(50, 24)


hideturtle()
done()

