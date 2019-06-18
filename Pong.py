import turtle
import time
import random

wn=turtle.Screen()
wn.title("P!nG-PoNg")
wn.bgcolor("#00FFFF")
wn.setup(width=800, height=700)
wn.tracer(0) # Turns off the screen updates

delay = 0.1
y_dir=12
x_dir=15

score1 = 0
score2 = 0

#slate 1
slate1 = turtle.Turtle()
slate1.speed(0)
slate1.shape("square")
slate1.color("#00008B")
slate1.shapesize(stretch_wid=5, stretch_len=1)
slate1.penup()
slate1.goto(-350,0)
slate1.direction = "stop"

# Slate 2
slate2 = turtle.Turtle()
slate2.speed(0)
slate2.shape("square")
slate2.color("#00008B")
slate2.shapesize(stretch_wid=5, stretch_len=1)
slate2.penup()
slate2.direction="stop"
slate2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#FF4040")
ball.penup()
ball.goto(0,0)
ball.direction = "stop"

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#FF4040")
pen.penup()
pen.hideturtle()
pen.goto(10, 300)
pen.write("score1: 0  score2: 0",align="center", font=("Courier", 16, "normal"))

# Functions
def go_up():
	slate1.direction = "up"
	move1()
def go_down():
	slate1.direction = "down"
	move1()
def gogo_up():
	slate2.direction = "up"
	move2()
def gogo_down():
	slate2.direction = "down"
	move2()

def move1():
	if slate1.direction == "up":
		y = slate1.ycor()
		slate1.sety(y + 20)
	if slate1.direction == "down":
		y = slate1.ycor()
		slate1.sety(y - 20)
def move2():
	if slate2.direction == "up":
		y = slate2.ycor()
		slate2.sety(y + 20)
	if slate2.direction == "down":
		y = slate2.ycor()
		slate2.sety(y - 20)
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(gogo_up, "Up")
wn.onkeypress(gogo_down, "Down")
def move_ball():
	x=ball.xcor()
	y=ball.ycor()
	ball.setx(x+x_dir)
	ball.sety(y+y_dir)
# Main game loop
while True:
	pen.clear() # Update the score display
	pen.write("Score1: {}  Score2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))
	wn.update()
	#move()  
	move_ball()
	if ball.xcor()>360 :
		score1+=10
		ball.goto(0,0)
		x_dir*=-1
		pen.clear() # Update the score display
		pen.write("Score1: {}  Score2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))
	if ball.xcor()<-360  :
		score2+=10
		ball.goto(0,0)
		x_dir*=-1
		pen.clear() # Update the score display
		pen.write("Score1: {}  Score2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))

	if ball.ycor()>350 or ball.ycor()<-350:
		y_dir*=-1
	#Paddle and ball collisions
	if slate1.distance(ball)<20 or (ball.xcor()<-340 and ball.xcor()>-350 and slate1.xcor()-ball.xcor()>-20 and (slate1.ycor()-ball.ycor()>-40 or slate1.ycor()-ball.ycor()<40)):
		x_dir*=-1
		score1+=10
		move_ball()
	if slate2.distance(ball)<20 or (ball.xcor()>340 and ball.xcor()<350 and slate2.xcor()-ball.xcor()<30 and (slate2.ycor()-ball.ycor()<0 or slate2.ycor()-ball.ycor()>-40)):
		x_dir*=-1
		score2+=10
		move_ball()	
			
	time.sleep(delay)
root.mainloop()
wn.mainloop()