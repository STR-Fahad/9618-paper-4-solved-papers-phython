global HashTable,Spare
HashTable=[]
Spare=[]

class Record:
    def __init__(self,I1,I2,key):
        self.Key=key
        self.Item1=I1
        self.Item2=I2
    def GetItem1(self):
        return self.Item1
    def GetItem2(self):
        return self.Item2
    def GetKey(self):
        return self.Key
def Initilalise():
    for i in range(0,200):
        HashTable.append(Record(-1,-1,-1))
    for x in range(0,100):
        Spare.append(Record(-1,-1,-1))
def CalculateHaash(Key):
    return Key%200
def InsertIntoHash(Record):
    global HashTable,Spare
    HashVal=CalculateHaash(Record.GetKey())
    if HashTable[HashVal].Getkey()==-1:
        HashTable[HashVal]=Record
    else:
        for x in range(0,100):
            if Spare[x].getKey()==-1:
                Spare[x]=Record
                break
def CreateHashTable():
    global HashTable,Spare
    try:
         File=open("HashData.txt","r")
         for Line in File:
             Data=Line.strip()
             Data=Line.strip(",")
             InsertIntoHash(Record(int(Data[0],Data[1],Data[2])))
         File.close()
    except:
        print("File cannot be found")
def PrintSpare():
    global HashTable,Spare
    x=0
    while Spare[x].GetKey()==-1:
        print(Spare[x].Getkey())
        x+=1

