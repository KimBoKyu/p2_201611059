import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.penup()
t2=turtle.Turtle()
t2.penup()
t2.goto(-100,100)
t2.pendown()
t2.fd(200)
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
    (x,y)=t1.pos() 
    if -80<x<80 and 95<y<105:
        print "Correct"

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