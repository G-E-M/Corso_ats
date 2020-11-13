import turtle


start_angle = 36
seg_lenght = 100
t = turtle.Turtle()
t.pencolor("green")
t.pensize(10)
for i in range(5):
    if i % 2 == 0:
        t.forward(seg_lenght)
    else:
        t.backward(seg_lenght)
    t.left(start_angle)