from tkinter import CENTER
import turtle
import winsound

sc = turtle.Screen()
sc.title("Ping Pong by David Kim")
sc.bgpic("backg2.gif")
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.tracer(0)


score = turtle.Turtle()
score.speed(0)
score.color("red")
score.hideturtle()
score.write("Iron Man : 0 vs Captain America: 0",
            align="center", font=("Verdana", 27, "normal"))

s_Iron = 0
s_Captain = 0


a_side = turtle.Turtle()
a_side.speed(0)
a_side.shape("square")
a_side.color("light green")
a_side.shapesize(stretch_wid=5, stretch_len=1)
a_side.penup()
a_side.goto(-350, 0)


def a_up():
    y = a_side.ycor()
    y += 20
    a_side.sety(y)


def a_down():
    y = a_side.ycor()
    y -= 20
    a_side.sety(y)


sc.listen()
sc.onkeypress(a_up, "w")
sc.onkeypress(a_down, "s")

b_side = turtle.Turtle()
b_side.speed(0)
b_side.shape("square")
b_side.color("light green")
b_side.shapesize(stretch_wid=5, stretch_len=1)
b_side.penup()
b_side.goto(350, 0)


def b_up():
    y = b_side.ycor()
    y += 20
    b_side.sety(y)


def b_down():
    y = b_side.ycor()
    y -= 20
    b_side.sety(y)


sc.listen()
sc.onkeypress(b_up, "Up")
sc.onkeypress(b_down, "Down")

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


while True:
    sc.update()

    ball.setx(ball.xcor()+(ball.dx/2))
    ball.sety(ball.ycor()+(ball.dy/2))

    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)

    if(ball.ycor() < - 290):
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)
    if(ball.xcor() < -390):
        ball.dx *= -1
        ball.goto(0, 0)
        score.clear()
        s_Captain += 1
        score.write("Iron Man : {} vs Captain America: {}".format(
            s_Iron, s_Captain), align="center", font=("Verdana", 27, "normal"))

    if(ball.xcor() > 390):
        ball.dx *= -1
        ball.goto(0, 0)
        score.clear()
        s_Iron += 1
        score.write("Iron Man : {} vs Captain America: {}".format(
            s_Iron, s_Captain), align="center", font=("Verdana", 27, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < b_side.ycor() + 50 and ball.ycor() > b_side.ycor()-50):
        ball.dx *= -1
        ball.setx(340)
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < a_side.ycor() + 50 and ball.ycor() > a_side.ycor()-50):
        ball.dx *= -1
        ball.setx(-340)
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)
    if a_side.ycor() > 250:
        a_side.sety(250)

    if a_side.ycor() < - 250:
        a_side.sety(-250)

    if b_side.ycor() > 250:
        b_side.sety(250)

    if b_side.ycor() < - 250:
        b_side.sety(-250)
