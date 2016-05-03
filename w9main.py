import matplotlib
import matplotlib.pyplot as plt
mh=set(['TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'])
fh=set(['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'])
mh1=['TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder']
fh1=['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder']
word1 = "sangmyung university"
word2 = "7 hongjidong"

def charCount(word1):
    d=dict()
    for c in word1:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    plt.bar(range(0,len(d)),d.values(), align='center')
    plt.xticks(range(0,len(d)),list(d.keys()))
    plt.show()


def countDigitsLetters(word2):
    d={"number":0, "word":0}
    for c in word2:
        if c.isdigit()==True:
            d["number"]=d["number"]+1
        elif c.isdigit()==False:
            d["word"]=d["word"]+1
    print d
    plt.bar(range(0,len(d)),d.values(), align='center')
    plt.xticks(range(0,len(d)),list(d.keys()))
    plt.show()

def myhome():
    print "Only in my home is ", mh.difference(fh)

def yourhome():
    print "Only in friend home is ", fh.difference(mh)

def ourhome():
    print "Intersection our home is ", mh.intersection(fh)

def mhandyh():
    print "My home and friend home is ", mh1+fh1
    for c in fh1:
        mh1.append(c)
    d=dict()
    for e in mh1:
        if e not in d:
            d[e]=1
        else:
            d[e]=d[e]+1
    print d



def lab9():
    print "To next, Close graph!!"
    charCount(word1)
    countDigitsLetters(word2)
    print "To next, Close graph!!"
    myhome()
    yourhome()
    ourhome()
    mhandyh()

def main():
    lab9()
    raw_input()

if __name__=="__main__":
    main()
