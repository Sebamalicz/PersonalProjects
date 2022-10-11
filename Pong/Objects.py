import turtle
Width = 800
Height = 600

class Paddle:

    def __init__(self, startX):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(startX, 0)
      
    def paddleUp(self):
        y = self.paddle.ycor()
        if not y + 20 + 50 >= 300:
            y += 20
        else:
            y += 300 - y - 50 
        self.paddle.sety(y)

    def paddleDown(self):
        y = self.paddle.ycor()
        if not y - 20 - 50 <= -300:
            y -= 20
        else:
            y -= 300 + y - 50
        self.paddle.sety(y)

class Ball:

    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = 2
        self.ScoreA = 0
        self.ScoreB = 0
    
    def xMove(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)

    def yMove(self):
        self.ball.sety(self.ball.ycor() + self.ball.dy) 

    def borderCheck(self):
        if self.ball.ycor() + 10 == 300 or self.ball.ycor() - 20 == -300:
            self.ball.dy = - self.ball.dy
        
        if self.ball.xcor() + 20 == 400:
            self.ball.dx = -self.ball.dx
            self.ball.goto(0, 0)
            self.ScoreA += 1

        if self.ball.xcor() - 10 == -400:
            self.ball.dx = - self.ball.dx
            self.ball.goto(0, 0)
            self.ScoreB += 1 

    def updateDx(self):
        self.ball.dx = -self.ball.dx

    def updateDy(self):
        self.ball.dy = -self.ball.dy

class Pen:

    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Player A: 0   Player B: 0", align = "center", font = ("Courier", 24, "normal"))

    def updateScore(self, ScoreA, ScoreB):
        self.pen.clear()
        self.pen.write("Player A: {}   Player B: {}".format(ScoreA, ScoreB), align = "center", font = ("Courier", 24, "normal"))
