import turtle
import math
import time
t1=turtle.Turtle()
t2=turtle.Turtle()
wn = turtle.Screen()
t2.shape("turtle")
t2.color("Brown")
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
def getCoordsFromFile():
    filehome=open('circle.txt')
    coords=list()
    for line in filehome:
        cirpos=line.split(',')
        coords.append([cirpos[0],cirpos[1], cirpos[2],cirpos[3], cirpos[4],cirpos[5].strip()])
    filehome.close()
    return coords
coords=getCoordsFromFile()

def Circle(coords):
    for coord in coords:
        x1=int(coords[0][0])
        y1=int(coords[0][1])
        x2=int(coords[0][2])
        y2=int(coords[0][3])
        x3=int(coords[0][4])
        y3=int(coords[0][5])
    t1.penup()
    t1.color("red")
    t1.goto(x1,y1)
    t1.fillcolor("RED")
    t1.pendown()
    t1.begin_fill()
    t1.circle(40)
    t1.end_fill()
    t1.setheading(0)
    t1.penup()
    t1.color("pink")
    t1.goto(x2,y2)
    t1.fillcolor("pink")
    t1.pendown()
    t1.begin_fill()
    t1.circle(30)
    t1.end_fill()
    t1.setheading(0)
    t1.penup()
    t1.color("Yellow")
    t1.goto(x3,y3)
    t1.fillcolor("Yellow")
    t1.pendown()
    t1.begin_fill()
    t1.circle(50)
    t1.end_fill()
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
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if -215<x<=-150 and 100<=y<=176:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if -235<=x<=-215 and 151<=y<=176:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if -235<=x<=-215 and 140<=y<=151:
        result=result+4
        print("Your point is %d !" % result)
        t2.goto(0,-200)
def squ():
    (x,y)=t2.pos()
    global result
    if -100<=x<-35 and 100<=y<=250:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if -15<x<=50 and 100<=y<=250:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if -35<=x<=-15 and 185<=y<=250:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if -35<=x<=-15 and 165<=y<=185:
        result=result+5
        print("Your point is %d !" % result)
        t2.goto(0,-200)
def bar():
    (x,y)=t2.pos()
    global result
    if 80.<=x<=280. and 239.<=y<=245.: 
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if 130.<=x<=230. and 189.<=y<=195.:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if 190.<=x<=230. and 139.<=y<=145.:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if 130.<=x<=280. and 89.<=y<=95.:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if 90.<=y<=240. and 279.<=x<=285.:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if 140.<=y<=190. and 229.<=x<=235.:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if 90.<=y<=190. and 129.<=x<=135.:
        result=result-1
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if 210<=x<=230 and 155<=y<=185:
        result=result+7
        print("Your point is %d !" % result)
        t2.goto(0,-200)
def cir():
    (x,y)=t2.pos()
    global result
    if math.sqrt(math.pow(x,2) + math.pow((-10-y),2))<=40:
        result=result-2
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if math.sqrt(math.pow((-200-x),2) + math.pow((-50-y),2))<=30:
        result=result-2
        print("Your point is %d !" % result)
        t2.goto(0,-200)
    if math.sqrt(math.pow((180-x),2) + math.pow((-50-y),2))<=50:
        result=result-2
        print("Your point is %d !" % result)
        t2.goto(0,-200)
def score():
    played=open('save.txt', 'a')
    if result>=20:
        name = raw_input("Put in your name: ")
        msg='played {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print("End Game"+'\n'+'Score' + '\t'+ str(result) +'\t' + msg)
        played.write('\n' + 'Score' + '\t'+ str(result) +'\t' + msg)
        played.close()
        print("Click Screen")
	wn.exitonclick()
    if result<= -15:
        print("You lose!!!! Click Screen")
	wn.exitonclick()
def background():
    Circle(coords)
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
def alarm():
    print("You can move to press Key, Avoid Circle~!!")
    print("In Triangle = 4 point")
    print("In Square = 5 point")
    print("In Miro = 7 point")
    print("In line = -1 point")
    print("In Circle = -2 point")
alarm()
background()
addkeys()
wn.listen()
turtle.mainloop()