import turtle

seq = ['green','red','blue','yellow','purple','lightblue']
c_offset = 0 
t = turtle.Turtle()
for i in range(3):
    for c in seq:
        for f in range(4):
            t.down()
            t.pencolor(c)
            t.forward(10)
            t.right(90)
            t.forward(10)

        t.up()
        t.forward(60)
    t.home()
    t.up()
    c_offset += 60
    t.right(90)
    t.forward(c_offset)
    t.right(-90)
        
    
