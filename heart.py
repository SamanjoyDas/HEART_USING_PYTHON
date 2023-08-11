import turtle
wn = turtle.Screen()
wn.setup(width=400, height=400)
t = turtle.Turtle() # Assigning "t" as name of the turtle

def curve(): # Method to draw curve
    for i in range(200): # To draw the curve step by step
        t.right(1)
        t.forward(1)

def heart():  # Method to draw full Heart
    t.fillcolor('pink')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve() # Left Curve
    t.left(120)
    curve() # Right Curve
    t.forward(112)
    t.end_fill()

heart()
t.ht() # Hiding Turtle
turtle.done()
