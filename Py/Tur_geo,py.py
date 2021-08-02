import turtle
turtle.setup(width=600, height=500)
turtle.reset()
turtle.hideturtle()
turtle.speed(0)

turtle.bgcolor('black')

c=0
x=0

colors = ["red","orange","yellow","green","blue","red","orange","yellow","green","blue",
"red","orange","yellow","green","blue","red","orange","yellow","green","blue""red","orange","yellow","green","blue",
"red","orange","yellow","green","blue","red","orange","yellow","green","blue","red","orange","yellow","green","blue",
"red","orange","yellow","green","blue","red","orange","yellow","green","blue","red","orange","yellow","green","blue""red","orange","yellow","green","blue"]
while x < 500:
    idx = int(c)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(98)
    x = x + 0.5
    c = c + 0.1

turtle.done()
