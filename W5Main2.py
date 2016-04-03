import turtle
wn=turtle.Screen()
def Game():
    print "Select Rock Scissors Paper"
    UserA = raw_input("A : ")
    UserB = raw_input("B : ")
    def Number(USER):
        if(USER=="Rock"):
            return 1.0
        elif(USER=="Scissors"):
            return 2.0
        elif(USER=="Paper"):
            return 4.0
        else:
            print "input error"
    s = Number(UserA)/Number(UserB)
    if(s==1.0):
        print "No Winner"
    elif(s==0.5):
        print "A is Winner"
    elif(s==0.25):
        print "B is Winner"
    elif(s==2):
        print "B is Winner"
    elif(s==4):
        print "A is Winner"

def replay():
	sel=raw_input("Do you want one more time? y or n : ")
	if(sel=='y'):
		rsp()
	else:
		print "Click white Screen! Good Bye~"
def rsp():
	Game()
	replay()
rsp()

wn.exitonclick()