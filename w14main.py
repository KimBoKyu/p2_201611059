Dogname=raw_input("Dog name :")
Dogtalk=raw_input("Dog talk :")
class Dog(object):
    def __init__(self, name, sound):
        self.name=name
        self.sound=sound
    def talkDog(self):
        print self.name, "talk", self.sound
question=Dog(Dogname, Dogtalk)
question.talkDog()