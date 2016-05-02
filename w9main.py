import matplotlib
import matplotlib.pyplot as plt

def charCount(word):
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    print d
    plt.bar(range(0,len(d)),d.values(), align='center')
    plt.xticks(range(0,len(d)),list(d.keys()))
    plt.show()


def lab9():
    word = 'sangmyung university'
    charCount(word)

def main():
    lab9()
    raw_input()

if __name__=="__main__":
    main()



