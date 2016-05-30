import turtle
import math
import time
t1=turtle.Turtle()
t2=turtle.Turtle()
wn = turtle.Screen()
t2.shape("turtle")
t2.color("YELLOW")
t1.speed(5)
t2.penup()
t2.goto(0,-220)
t2.setheading(90)
result=0
def Triangle():
    t1.color("Purple")
    t1.penup()
    t1.goto(-300,100)
    t1.pendown()
    t1.fillcolor("Purple")
    t1.begin_fill()
    t1.fd(65)
    t1.penup()
    t1.fd(20)
    t1.pendown()
    t1.fd(65)
    for i in range(0,2):
        t1.lt(120)
        t1.fd(150)
    t1.penup()
    t1.end_fill()
    t1.color("white")
    t1.fillcolor("white")
    t1.lt(120)
    t1.fd(65)
    t1.lt(90)
    t1.pendown()
    t1.begin_fill()
    t1.fd(40)
    t1.pendown()
    t1.rt(90)
    for a in range(0,4):
        t1.fd(20)
        t1.lt(120)
    t1.rt(210)
    t1.fd(40)
    t1.end_fill()
    t1.setheading(0)
def Square():
    t1.color("Green")
    t1.penup()
    t1.goto(-100,100)
    t1.pendown()
    t1.fillcolor("Green")
    t1.begin_fill()
    t1.fd(60)
    t1.penup()
    t1.fd(30)
    t1.pendown()
    t1.fd(60)
    for i in range(0,3):
        t1.lt(90)
        t1.fd(150)
    t1.end_fill()
    t1.penup()
    t1.color("white")
    t1.fillcolor("white")
    t1.lt(90)
    t1.fd(65)
    t1.begin_fill()
    t1.pendown()
    t1.lt(90)
    t1.fd(65)
    for b in range(0,3):
        t1.fd(20)
        t1.rt(90)
    t1.lt(90)
    t1.fd(65)
    t1.end_fill()
    t1.setheading(0)
def Circle():
    t1.color("red")
    t1.penup()
    t1.goto(0,-50)
    t1.pendown()
    t1.circle(40)
    t1.setheading(0)
def baram():
    size=200
    t1.stamp()
    t1.color("blue")
    t1.fillcolor("skyblue")
    t1.penup()
    t1.goto(80,240)
    t1.pendown()
    t1.begin_fill()
    for i in range(0,9):
        t1.fd(size)
        t1.rt(90)
        if i%2==0:
            size=size-50
    t1.end_fill()
    t1.setheading(0)
def tri():
    (x,y)=t2.pos()
    global result
    if -300<=x<-235 and 100<=y<=176:
        print "False"
        t2.goto(0,-200)
    if -215<x<=-150 and 100<=y<=176:
        print "False"
        t2.goto(0,-200)
    if -235<=x<=-215 and 151<=y<=176:
        print "False"
        t2.goto(0,-200)
    if -235<=x<=-215 and 140<=y<=151:
        result=result+2
        print "Your point is %d !" % result
        t2.goto(0,-200)
def squ():
    (x,y)=t2.pos()
    global result
    if -100<=x<-35 and 100<=y<=250:
        print "False"
        t2.goto(0,-200)
    if -15<x<=50 and 100<=y<=250:
        print "False"
        t2.goto(0,-200)
    if -35<=x<=-15 and 185<=y<=250:
        print "False"
        t2.goto(0,-200)
    if -35<=x<=-15 and 165<=y<=185:
        result=result+3
        print "Your point is %d !" % result
        t2.goto(0,-200)
def bar():
    (x,y)=t2.pos()
    global result
    if 80.<=x<=280. and 239.<=y<=241.: 
        t2.goto(0,-200)
    if 130.<=x<=230. and 189.<=y<=191.:
        t2.goto(0,-200)
    if 190.<=x<=230. and 139.<=y<=141.:
        t2.goto(0,-200)
    if 130.<=x<=280. and 89.<=y<=91.:
        t2.goto(0,-200)
    if 90.<=y<=240. and 279.<=x<=281.:
        t2.goto(0,-200)
    if 140.<=y<=190. and 229.<=x<=231.:
        t2.goto(0,-200)
    if 90.<=y<=190. and 129.<=x<=131.:
        t2.goto(0,-200)
    if 210<=x<=230 and 155<=y<=185:
        result=result+4
        print "Your point is %d !" % result
        t2.goto(0,-200)
def cir():
    (x,y)=t2.pos()
    global result
    if math.sqrt(math.pow(x,2) + math.pow(y,2))<=40:
        result=result+10
        print "Your point is %d !" % result
        t2.goto(0,-200)
def score():
    played=open('save.txt', 'a')
    if result>=20:
        name = raw_input("Put in your name: ")
        msg='played {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print "End Game"+'\n'+'Score' + '\t'+ str(result) +'\t' + msg
        played.write('\n' + 'Score' + '\t'+ str(result) +'\t' + msg)
        played.close()
        print "Click Screen"
def background():
    Circle()
    Triangle()
    Square()
    baram()
def keyup(): 
    t2.fd(15)
    tri()
    squ()
    bar()
    cir()
    score()
def keydown(): 
    t2.back(10) 
def turnr(): 
    t2.right(30) 
def turnl(): 
    t2.left(30) 
def addkeys(): 
    wn.onkey(keyup, "Up") 
    wn.onkey(keydown, "Down") 
    wn.onkey(turnr, "Right") 
    wn.onkey(turnl, "Left") 
print "Don't use mouse!!!!!"
print "In Circle = 1point"
print "In Triangle = 2point"
print "In Square = 3point"
print "In Miro = 4point"
background()
addkeys()
wn.listen()
wn.exitonclick()


