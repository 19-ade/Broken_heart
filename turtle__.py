import turtle
import time

wn = turtle.Screen()
wn.title("ANDE")
wn.bgcolor("white")



player = turtle.Turtle()
player.speed(0)
player.width(12)

def curve():
	for i in range(200):
		player.right(1)

		player.forward(1)

def heart():
	player.color('red', 'red')
	player.begin_fill()
	player.left(140)
	player.forward(110)
	curve()
	player.left(120)
	curve()
	player.forward(112)
	player.end_fill()

heart()
player.pencolor('white')
player.penup()
player.goto(0, 170)
player.pendown()

for i in range(3):
	player.left(75)
	player.forward(49)
	player.right(65)
	player.forward(40)

wn.mainloop()