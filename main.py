import turtle

s = turtle.Screen()
s.bgcolor("#05192D")
s.setup(width=550, height=370)
s.title("Drawing Lines Practice")

a = turtle.Turtle()
a.pensize(7)
a.shape("turtle")

a.penup()
a.backward(100)
a.pendown()

# the vertical line (main line)
a.pencolor("#FFFFFF")
a.left(90)
a.forward(100)
a.right(150)
a.forward(115)
a.left(130)
a.forward(110)
a.right(140)
a.forward(110)

a.penup()
a.goto(-100, 100)
a.pendown()

a.pencolor("#03EF62")
a.setheading(0)
a.penup()
a.forward(15)
a.pendown()
a.forward(45)
a.right(120)
a.forward(45)

a.penup()
a.goto(-15, 40)
a.pendown()
a.setheading(0)
a.forward(20)

a.penup()
a.goto(-20, 30)
a.pendown()
a.setheading(0)
a.forward(30)

a.hideturtle()
turtle.done()