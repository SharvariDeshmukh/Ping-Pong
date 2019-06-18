import turtle
import time
import random
import winsound 
wn=turtle.Screen()
wn.title("P!nG-PoNg")
wn.bgcolor("#000000")
wn.setup(width=800, height=700)
wn.tracer(0) # Turns off the screen updates
t=5
a=0
m=1
delay = 0.1
y_dir=12
x_dir=15

score1 = 0
score2 = 0

#slate 1
slate1 = turtle.Turtle()
slate1.speed(0)
slate1.shape("square")
slate1.color("#00BFFF")
slate1.shapesize(stretch_wid=5, stretch_len=1)
slate1.penup()
slate1.goto(-350,0)
slate1.direction = "stop"

# Slate 2
slate2 = turtle.Turtle()
slate2.speed(0)
slate2.shape("square")
slate2.color("#00BFFF")
slate2.shapesize(stretch_wid=5, stretch_len=1)
slate2.penup()
slate2.direction="stop"
slate2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#FFFF00")
ball.penup()
ball.goto(0,0)
ball.direction = "stop"

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("#FDF5E6")
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
	slate2.shapesize(stretch_wid=t, stretch_len=1)
	slate1.shapesize(stretch_wid=t, stretch_len=1)
	a=a+0.125
	wn.update()
	#move()  
	move_ball()
	if ball.xcor()>400 :
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		score1+=10
		time.sleep(1)
		ball.goto(0,0)
		x_dir*=-m
		
		
	elif ball.xcor()<-400  :
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		score2+=10
		time.sleep(1)
		ball.goto(0,0)
		x_dir*=-m
	elif ball.ycor()>350 or ball.ycor()<-350:
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		y_dir*=-m
	#Paddle and ball collisions
	elif (ball.xcor()<-340 and ball.xcor()>-350 and (slate1.ycor()-ball.ycor()>-50 and slate1.ycor()-ball.ycor()<50)):
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		x_dir*=-m
		score1+=10
		move_ball()
	elif (ball.xcor()>340 and ball.xcor()<350 and (slate2.ycor()-ball.ycor()<50 and slate2.ycor()-ball.ycor()>-50)):
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
		x_dir*=-m
		score2+=10
		move_ball()	
	pen.clear() # Update the score display
	pen.write("Score1: {}  Score2: {}".format(score1, score2), align="center", font=("Courier", 16, "normal"))		
	time.sleep(delay)
	if a%10==0 and t>1:
		t=t-1
	elif t==1:
		t=5
		move_ball()
root.mainloop()
wn.mainloop()