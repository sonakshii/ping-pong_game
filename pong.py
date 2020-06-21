import turtle
import winsound

wn= turtle.Screen()
wn.title("PONG GAME")
wn.bgcolor("black")
wn.setup( width= 800, height= 600)
wn.tracer(0)

score_a=0
score_b=0

paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=.215
ball.dy=.215

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLAYER A: 0  PLAYER B: 0",align="center", font=("Courier",24,"normal"))

def a_up():
    y = paddle_a.ycor()
    if(paddle_a.ycor()==260):
        y=y
    else:
        y+=20
    paddle_a.sety(y)
def a_down():
    y = paddle_a.ycor()
    if (paddle_a.ycor() ==-240):
        y = y
    else:
        y -= 20
    paddle_a.sety(y)
def b_up():
    y = paddle_b.ycor()
    if (paddle_b.ycor() == 260):
        y = y
    else:
        y += 20
    paddle_b.sety(y)
def b_down():
    y = paddle_b.ycor()
    if (paddle_b.ycor() == -240):
        y = y
    else:
        y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(a_up, "w")
wn.onkeypress(a_down,"s")
wn.onkeypress(b_up,"Up")
wn.onkeypress(b_down,"Down")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor()>390:
        ball.setx(390)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("PLAYER A: {}  PLAYER B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("PLAYER A: {}  PLAYER B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ( ball.xcor()>340 and ball.xcor()<350 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif( ball.xcor()<-340 and ball.xcor()>-350 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)