import matplotlib
import matplotlib.pyplot as plt

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

def lab9():
    word1 = "sangmyung university"
    charCount(word)
    word2 = "7 hongjidong"
    countDigitsLetters(word2)

def main():
    lab9()
    raw_input()

if __name__=="__main__":
    main()



