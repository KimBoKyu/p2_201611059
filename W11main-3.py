import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("C:\Users\P400\Desktop\miro.gif")
t1.pencolor("RED")
t1.shape("turtle")
t1.speed(1)
t1.penup()
t1.goto(-320,300)
t1.clear()
def keyup():
    t1.fd(50)
def keydown():
    t1.back(50)
def turnr():
    t1.right(90)
def turnl():
    t1.left(90)
def mousegoto(x,y):
    t1.setpos(x,y)
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