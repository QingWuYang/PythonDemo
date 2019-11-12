import turtle as T
import math

def writeNS(T):
    T.penup()
    T.backward(20)
    T.setheading(90)
    T.pendown()

    # 画左边的手柄
    T.forward(200)
    T.setheading(180)
    T.forward(50)
    T.circle(25, 90)
    T.forward(150)
    T.circle(25, 90)
    T.forward(50)
    T.penup()

    T.goto(20, 0)

    # 画右边的手柄
    T.fillcolor(0, 0, 0)
    T.begin_fill()
    T.pendown()
    T.setheading(90)
    T.pendown()
    T.forward(200)
    T.setheading(0)
    T.forward(50)
    T.circle(-25, 90)
    T.forward(150)
    T.circle(-25, 90)
    T.forward(50)
    T.end_fill()

    # 画左边中间的园
    T.hideturtle()
    T.pensize(5)
    T.penup()
    T.goto(-55, 130)
    T.fillcolor(0, 0, 0)
    T.begin_fill()
    T.pendown()
    T.setheading(0)
    T.circle(20)
    T.end_fill()

    # 画左边中间的园
    T.hideturtle()
    T.pensize(5)
    T.penup()
    T.goto(55, 70)
    T.fillcolor(254, 96, 83)
    T.begin_fill()
    T.pendown()
    T.setheading(0)
    T.circle(-20)
    T.end_fill()


T.shape("turtle")
T.colormode(255)
T.bgcolor(254, 96, 83)
T.screensize(500, 500)
T.pensize(10)
T.pencolor("black")
T.hideturtle()
# T.speed()

writeNS(T)
T.penup()
T.goto(-95, -50)
T.write("NINTENDO", font=("Arial", 38, "normal"))
T.penup()
T.goto(-95, -100)
T.write("SWITCH", font=("Arial", 50, "bold"))


T.exitonclick()
