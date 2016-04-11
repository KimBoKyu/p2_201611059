"""
@author KBK
@since 160411
"""
def sumList(aList):
    x=list()
    for i in range(0,aList):
        if (i%4== 0 and i%5 != 0):
            x.append(i)
    sum = 0
    for b in range(0,len(x)):
        sum = sum+x[b]
    return sum
    
def lab6():
    aList=1001
    labsum=sumList(aList)
    print labsum

def main():
    lab6()

if __name__=="__main__":
        main()
wn = raw_input("If you want to exit program, Press Enter!")
