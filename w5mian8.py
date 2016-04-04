height = input("Put in your height : ")
weight = input("Put in your weight : ")
BMI =  weight * 10000 / (height * height)
print BMI

if BMI < 18.5 :
    print "low weight"
elif BMI >= 18.5 and BMI < 25 :
    print "nomal weight"
elif BMI >= 25 and BMI < 30 :
    print "overweight"
elif BMI >= 30 and BMI < 35 :
    print "little overweight"
elif BMI > 35 :
    print "super overweight"
else :
    print "Input Error"