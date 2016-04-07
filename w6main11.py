"""
@author KBK
@since 160407
"""


def UpDown():
	import random
	ai = input("Select your Max range  ")
	r1 = random.randrange(1,ai+1)
	global pl
	print "Let's Start up & down game!!!"


	def game():
	    pl = input("Select you thinking numbers!  ")
	    if (r1>pl):
	        result = "Up"
	        print result
	        game()
	    elif (r1<pl):
	        result = "Down"
	        print result
	        game()
	    else :
	        result = "Correct"
	        print result
        	if (result=="Correct"):
	            wn = raw_input("Congratulations~!  Speak your feeling~  ")
	game()

"""
@startuml
title Up & Down Game
start
:Player : Select max range;
:Computer AI : Select random one number in range;
:Let's start Up & Down Game!!!!;
:Player input one number; 
while(Play)
if (Compare Player N & AI N) then (Plater N < AI N)
:Up;
else (Player N > AI B)
:Down;
endif
endwhile
:Player N = AI N;
:"Congratulations~! Speak your feeling";
:End Game;
stop
@enduml
"""



def Leaf():
	year = input("This year is leap year??")
	if (year%4 == 0) and (year%100 !=0 or year%400==0):
	    print "YES"
	else:
	    print "NO"
	wn = raw_input()

"""
%%plantuml
@startuml
start
title When is leap yaer

:This year is leap year??;
if (year is divided by 4 and year is divided by 100 or divided by 400) then (correct)
    :print "YES";
else (non correct)
    :print "NO";
endif
stop

@enduml
"""

def lab6():
    UpDown()
    Leaf()
	
def main():
    lab6()

if __name__=="__main__":
    main()