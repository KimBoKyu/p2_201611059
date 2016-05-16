import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def draw():
    t1.penup()
    t1.goto(50,100)
    t1.pendown()
    t1.fd(100)
    t1.penup()
    t1.home()

draw()
line1=[(50,100),(150,100)]
x1=line1[0][0]-1
y1=line1[0][1]-1
x2=line1[1][0]+1
y2=line1[1][1]+1
pos1=(x1,y1)
pos2=(x2,y2)

def isOnLine(point,pos1,pos2):
    if x1<=point[0]<=x2 and y1<=point[1]<=y2:
        t1.color("red")
        draw()
def keyup():
    t1.fd(50)
    point=t1.pos()
    isOnLine(point,pos1,pos2)
def keydown():
    t1.back(50)
def turnr():
    t1.right(90)
def turnl():
    t1.left(90)
def mousegoto(x,y):
    t1.setpos(x,y)
    point=t1.pos()
    isOnLine(point,pos1,pos2)
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