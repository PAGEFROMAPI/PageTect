import turtle
t=turtle.Turtle()
t.speed(5) #1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

# create a subprogram to draw a square

def drawSquare():
	for i in range(4):
		t.forward(100)
		t.right(90)

# call the subprogram
drawSquare()