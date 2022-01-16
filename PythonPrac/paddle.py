import turtle
import os

window = turtle.getscreen()
window.title("OOXOO")
window.bgcolor("black")
window.setup(width=800, height=600)     # (0,0) is at the center
window.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # defualt 20 x 20
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# score
score_a = 0
score_b = 0

# Function
# move the paddle up or down by 20 each time
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290: # board is 600, ball is 20
        ball.dy *= -1   # reverse the direction
        os.system("afplay bounce.mp3&")
    if ball.ycor() < -290:
        ball.dy *= -1
        os.system("afplay bounce.mp3&")
    if ball.xcor() > 390:
        ball.dx *= -1
        os.system("afplay bounce.mp3&")
    if ball.xcor() < -390:
        ball.dx *= -1
        os.system("afplay bounce.mp3&")

    # Paddle and ball collisions
    if (ball.xcor() > 330 and ball.xcor() < 360
    and ball.ycor() < paddle_b.ycor() + 40
    and ball.ycor() > paddle_b.ycor() - 40):
        os.system("afplay bounce.mp3&")
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B: {}".format(score_a, score_b),
            align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() < -330 and ball.xcor() > -360
    and ball.ycor() < paddle_a.ycor() + 40
    and ball.ycor() > paddle_a.ycor() - 40):
        os.system("afplay bounce.mp3&")
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b),
            align="center", font=("Courier", 24, "normal"))
