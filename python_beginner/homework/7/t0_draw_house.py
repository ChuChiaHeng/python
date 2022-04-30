'''
請使用def畫出10個，不同顏色的屋頂、房身，及位置的房子
顏色用list用代入
'''
import turtle
import random
def roof(x, y):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color(r/255, g/255, b/255)
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
def house(x, y):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    turtle.penup()
    turtle.pendown()
    turtle.color(r/255, g/255, b/255)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.end_fill()
for s in range(10):
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    roof(x,y)
    house(x,y)