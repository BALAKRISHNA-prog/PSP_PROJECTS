import turtle

turtle.bgcolor("blue")
turtle.pensize(2)
turtle.speed(0)
forw = 1
turt = turtle.Turtle()
turt.speed(0)
while True:
        turtle.forward(forw)
        turtle.left(90)
        turtle.left(1)
        forw +=1

turtle.hideturtle()
