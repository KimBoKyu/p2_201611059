import turtle
t1=turtle.Turtle()
t2=turtle.Turtle()
wn = turtle.Screen()
t2.shape("turtle")
t2.pencolor("YELLOW")
t2.color("YELLOW")
t1.speed(5)
size = 150
def Square(size):
    t1.pencolor("RED")
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
    t1.penup()
    t1.goto(-5,140)
    t1.write("*")
    t1.goto(0,152)
    t1.write ("Come here plus two point")

def Triangle(size):
    t1.pencolor("BLUE")
    for i in range(0,3):
        t1.fd(size)
        t1.right(120)
    t1.penup()
    t1.goto(-225,165)
    t1.write("*")
    t1.goto(-210,175)
    t1.write ("Come here plus one point")

def Star(size):
    t1.pencolor("GREEN")
    for i in range(0,5):
        t1.fd(size)
        t1.right(144)
    t1.penup()
    t1.goto(225,170)
    t1.write("*")
    t1.goto(229,175)
    t1.write ("Come here plus three point")

def background():
    t1.penup()
    t1.goto(-300,230)
    t1.pendown()
    Triangle(size)
    t1.penup()
    t1.goto(-80,230)
    t1.pendown()
    Square(size)
    t1.penup()
    t1.goto(150,210)
    t1.pendown()
    Star(size)
    t1.goto(500,500)
    t2.penup()
    t2.goto(0,-200)  
background()
x=float()
y=float()
point = 0    
def k1():
    (x,y)=t2.pos() 
    t2.forward(10)
    global point
    if -10<x<5 and 145<y<155:
        point=point+2
        print "Your point is %d !" % point
        t2.goto(0,-200)
    if 220<x<230 and 175<y<185:
        point=point+3
        print "Your point is %d !" % point
        t2.goto(0,-200)
    if -240<x<-210 and 150<y<185:
        point=point+1
        print "Your point is %d !" % point
        t2.goto(0,-200)
    if point>20:
        print "End Game!!!!"
        raw_input("Press Enter out game")    
def k2():
    t2.left(15)

def k3():
    t2.right(15)

def k4():
    t2.back(5)

wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")
wn.listen()
wn.exitonclick()
