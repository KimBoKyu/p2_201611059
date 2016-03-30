marksTmp = raw_input('성적을 입력하세요 (0~100)')
marks = float(marksTmp)
print "입력 값은",marks

if(90<=marks<=100):
    print "My grade is %s" % "A"
elif(80<=marks<90):
    print "My grade is %s" % "B"
elif(70<=marks<80):
    print "My grade is %s" % "C"
elif(60<=marks<70):
    print "My grade is %s" % "D"
else:
    print "My grade is %s" % "F"