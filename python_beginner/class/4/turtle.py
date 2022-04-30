import turtle
"""
a=0
while a<4:
    turtle.forward(150)
    turtle.left(90)
    a+=1
"""
"""
while a<3:
    turtle.forward(150)
    turtle.left(120)
    a+=1
"""
"""
while a<5:
    turtle.forward(150)
    turtle.left(150)
    turtle.forward(150)
    turtle.right(78)
    a+=1
"""
turtle.color('pink')
turtle.shape('turtle')
turtle.penup()
for step in range(3,201,2):
    turtle.stamp()
    turtle.forward(step)
    turtle.right(35)
