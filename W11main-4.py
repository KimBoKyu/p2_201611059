import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def draw():
    t1.penup()
    t1.goto(100,100)
    t1.pendown()
    for i in range(0,4):
        t1.fd(100)
        t1.left(90)
    t1.penup()
    t1.home()
def change():
    if 100<=x<=200 and 100<=y<=200:
        t1.color("red")
        draw()
draw()
def keyup():
    t1.fd(50)
    (x,y)=t1.pos()
    change()
def keydown():
    t1.back(50)
def turnr():
    t1.right(90)
def turnl():
    t1.left(90)
def mousegoto(x,y):
    t1.setpos(x,y)
    (x,y)=t1.pos()
    change()
def addkeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keydown, "Down")
    wn.onkey(turnr, "Right")
    wn.onkey(turnl, "Left")
def addmouse():
    wn.onclick(mousegoto)
addkeys()
addmouse()
wn.listen()
turtle.mainloop()
