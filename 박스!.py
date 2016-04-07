import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

t1.penup()

t1.setpos(-300,100)

t1.pendown()

t1.pencolor("BLUE")

def BOX(size,pos):
  t1.setheading(0)
  t1.setpos(pos)
  t1.pendown()
  t1.fd(size)
  t1.right(90)
  t1.fd(size)
  t1.right(90)
  t1.fd(size)
  t1.right(90)
  t1.fd(size)
  t1.penup()

pos1=((-300,100))

pos2=((-95,100))

pos3=((110,100))

size=150

BOX(size,pos1)

t1.pencolor("RED")

BOX(size,pos2)

t1.pencolor("GREEN")

BOX(size,pos3)

t1.setheading(0)
t1.setpos(-280,80)
t1.pendown()
t1.pencolor("BLUE")
t1.fd(70)
t1.right(120)
t1.fd(70)
t1.penup()
t1.setpos(-180,90)
t1.setheading(270)
t1.pendown()
t1.fd(80)
t1.penup()
t1.setpos(-230,-5)
t1.pendown()
t1.fd(37)
t1.left(90)
t1.fd(37)
t1.left(90)
t1.fd(37)
t1.left(90)
t1.fd(37)

t1.penup()
t1.setpos((-60,80))
t1.pencolor("RED")
t1.setheading(270)
t1.pendown()
t1.fd(65)
t1.left(90)
t1.fd(80)
t1.left(90)
t1.fd(65)
t1.back(33)
t1.left(90)
t1.fd(80)
t1.penup()
t1.setpos((-20,0))
t1.setheading(270)
t1.pendown()
t1.fd(30)
t1.penup()
t1.setpos(-60,-30)
t1.pendown()
t1.left(90)
t1.fd(90)

t1.penup()
t1.goto(140,80)
t1.pendown()
t1.pencolor("GREEN")
t1.setheading(0)
t1.fd(85)
t1.right(90)
t1.fd(70)
t1.penup()
t1.goto(130,-5)
t1.pendown()
t1.setheading(0)
t1.fd(120)
t1.goto(170,-5)
t1.setheading(270)
t1.fd(30)
t1.penup()
t1.goto(210,-5)
t1.pendown()
t1.setheading(270)
t1.fd(30)
wn.exitonclick()
