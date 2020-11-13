import turtle


lato_spirale = 5
t = turtle.Turtle()

for i in range(100):
    t.left(90)
    lato_spirale = lato_spirale + 5
    t.forward(lato_spirale)

