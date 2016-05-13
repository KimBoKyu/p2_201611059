alldata = [('content', 13.1, 37.1, 8.7, 1.5),
('method', 10.6, 34.6, 13.4, 1.9),
('strelation', 27.1, 40.0, 2.9, 1.5),
('prrelation', 16.2, 37.8, 6.8, 0.8),
('equipment', 11.4, 29.8, 14.8, 4.9),
('enviroment', 12.2, 26.5, 14.9, 4.4),
('subject', 13.5, 29.7, 11.1, 2.4),
('school', 13.7, 37.6, 4.1, 1.2)]

def data():
    verygood=list()
    for i in range(0,len(alldata)):
        verygood.append(alldata[i][1])
    good=list()
    for i in range(0,len(alldata)):
        good.append(alldata[i][2])
    bad=list()
    for i in range(0,len(alldata)):
        bad.append(alldata[i][3])
    verybad=list()
    for i in range(0,len(alldata)):
        verybad.append(alldata[i][4])
    sumvg=0
    for i in range(0,len(alldata)):
        sumvg = sumvg + verygood[i]
    sumg = 0
    for i in range(0,len(alldata)):
        sumg = sumg + good[i]
    goodsum = 0
    goodsum = sumvg + sumg
    print "Very good & good sum is ", goodsum
    average = 0
    gaverage = goodsum / len(alldata)
    print "Very good & good average is ", gaverage

    sumb=0
    for i in range(0,len(alldata)):
        sumb = sumb + bad[i]
    sumvb = 0
    for i in range(0,len(alldata)):
        sumvb = sumvb + verybad[i]
    badsum = 0
    badsum = sumb + sumvb
    print "Bad & Very bad sum is ", badsum

    baverage = 0
    baverage = badsum / len(alldata)
    print "Bad & Very bad average is ", baverage

def president():
    Washington = list()
    Washington = ("AMONG the vicissitudes incident to life no event could have filled me with greater anxieties than that of which the notification was transmitted by your order, and received on the 14th day of the present month.",
                  "On the one hand, I was summoned by my country, whose voice I can never hear but with veneration and love, from a retreat which I had chosen with the fondest predilection, and, in my flattering hopes, with an immutable decision, as the asylum of my declining years - a retreat which was rendered every day more necessary as well as more dear to me by the addition of habit to inclination, and of frequent interruptions in my health to the gradual waste committed on it by time.",
                  "On the other hand, the magnitude and difficulty of the trust to which the voice of my country called me, being sufficient to awaken in the wisest and most experienced of her citizens a distrustful scrutiny into his qualifications, could not but overwhelm with despondence one who (inheriting inferior endowments from nature and unpracticed in the duties of civil administration) ought to be peculiarly conscious of his own deficiencies.",
                  "In this conflict of emotions all I dare aver is that it has been my faithful study to collect my duty from a just appreciation of every circumstance by which it might be affected.",
                  "All I dare hope is that if, in executing this task, I have been too much swayed by a grateful remembrance of former instances, or by an affectionate sensibility to this transcendent proof of the confidence of my fellow-citizens, and have thence too little consulted my incapacity as well as disinclination for the weighty and untried cares before me, my error will be palliated by the motives which mislead me, and its consequences be judged by my country with some share of the partiality in which they originated."
                  )
    doc=Washington
    dw=dict()
    for line in doc:
        for c in line.split():
            if c not in dw:
                dw[c]=1
            else:
                dw[c]=dw[c]+1
    for v in range(len(dw)):
        if dw.values()[v]>=10:
            resultw = dw.keys()[v], dw.values()[v]
    bush=list()
    bush = ("Vice President Cheney, Mr. Chief Justice, President Carter, President Bush, President Clinton, reverend clergy, distinguished guests, fellow citizens:",
           "On this day, prescribed by law and marked by ceremony, we celebrate the durable wisdom of our Constitution, and recall the deep commitments that unite our country.",
           "I am grateful for the honor of this hour, mindful of the consequential times in which we live, and determined to fulfill the oath that I have sworn and you have witnessed.",
           "At this second gathering, our duties are defined not by the words I use, but by the history we have seen together. For a half century,",
           "America defended our own freedom by standing watch on distant borders. After the shipwreck of communism came years of relative quiet, years of repose, years of sabbatical —and then there came a day of fire.",
           "We have seen our vulnerability —and we have seen its deepest source. For as long as whole regions of the world simmer in resentment and tyranny —prone to ideologies that feed hatred and excuse murder — violence will gather, and multiply in destructive power, and cross the most defended borders, and raise a mortal threat.",
           "There is only one force of history that can break the reign of hatred and resentment, and expose the pretensions of tyrants, and reward the hopes of the decent and tolerant, and that is the force of human freedom.",
           "We are led, by events and common sense, to one conclusion: The survival of liberty in our land increasingly depends on the success of liberty in other lands.",
           "The best hope for peace in our world is the expansion of freedom in all the world.",
           "America's vital interests and our deepest beliefs are now one. From the day of our Founding, we have proclaimed that every man and woman on this earth has rights, and dignity, and matchless value, because they bear the image of the Maker of Heaven and earth.",
           "Across the generations we have proclaimed the imperative of self-government, because no one is fit to be a master, and no one deserves to be a slave.",
           "Advancing these ideals is the mission that created our Nation. It is the honorable achievement of our fathers.",
           "Now it is the urgent requirement of our nation's security, and the calling of our time.")
    doc2=bush
    db=dict()
    for line in doc2:
        for c in line.split():
            if c not in db:
                db[c]=1
            else:
                db[c]=db[c]+1
    for v in range(len(db)):
        if db.values()[v]>=10:
            resultb = db.keys()[v], db.values()[v]
    print "Washington most used word is ", resultw,"Bush most used word is ", resultb

def lab10():
    data()
    president()
def main():
    lab10()
    raw_input()
if __name__=="__main__":
    main()