"""
@author KBK
@since 160407
"""


import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
size = 100
pos = (50,50)
def drawSquareAtSave(size, pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)
        tracks.append(t1.pos())
    return tracks
    t1.penup()

def drawSquareFrom():
    tracks=((50,50),(50,100),(0,50),(0,0),(50,50))
    t1.pendown()
    for i in range(0,5):
        t1.goto(tracks[i])

def lab7():
    mytrack=drawSquareAtSave(size,pos)
    print mytrack
    drawSquareFrom()
    raw_input()

def main():
    lab7()

if __name__=="__main__":
    main()
