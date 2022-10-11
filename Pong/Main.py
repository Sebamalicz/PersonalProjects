import turtle
import Objects


def setScreen():
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

def checkCollision():
    if (ball.ball.xcor() + 10 >= 340 and ball.ball.xcor() + 10 <= 350) and (ball.ball.ycor() + 10 <= paddleB.paddle.ycor() + 50 and
        ball.ball.ycor() - 10 >= paddleB.paddle.ycor() - 50):
        ball.updateDx()
       
    if (ball.ball.xcor() - 10 <= -340 and ball.ball.xcor() - 10 >= -350) and (ball.ball.ycor() + 10 <= paddleA.paddle.ycor() + 50 and 
        ball.ball.ycor() - 10 >= paddleA.paddle.ycor() - 50):
        ball.updateDx()
      

wn = turtle.Screen() 
setScreen()
paddleA = Objects.Paddle(-350)
paddleB = Objects.Paddle(350)
ball = Objects.Ball()
pen = Objects.Pen()
scoreA = 0
scoreB = 0

while True:
    wn.listen()
    wn.onkeypress(paddleA.paddleUp, "w")
    wn.onkeypress(paddleA.paddleDown, "s")
    wn.onkeypress(paddleB.paddleUp, "Up")
    wn.onkeypress(paddleB.paddleDown, "Down")
    wn.update()
    ball.xMove()
    ball.yMove()
    ball.borderCheck()
    checkCollision()
    pen.updateScore(ball.ScoreA, ball.ScoreB)


    
