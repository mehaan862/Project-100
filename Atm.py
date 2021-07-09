class Atm():
    def __init__(self,atmcard,pinnumber):
        self.atmcard=atmcard
        self.pinnumber=pinnumber

    
    def getatmcard(self):
        print(self.atmcard)

    def getpinnumber(self):
        print(self.pinnumber)
 
Cash=Atm(1234,4321)
Cash.getatmcard()