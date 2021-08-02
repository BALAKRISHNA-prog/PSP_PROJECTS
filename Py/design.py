import turtle
forw = 1
turt = turtle.Turtle()
turt.speed(0)

for i in range(6):
    for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turt.forward(forw)
        turt.left(60)
        turt.left(1)
        forw += 1

turtle.done()
