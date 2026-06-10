class Record:
    def __init__(self,PKey,PData):
        self.Key=PKey
        self.Data=PData
global HashTable
HashTable=[]
def InitialiseHashTable():
    global HashTable
    HashTable=[[Record(-1,"")]*10 for i in range(100)]

def Hash(Key):
    return Key%100
def InsertData(DatatoAdd):
    global HashTable
    HashValue = Hash(DatatoAdd.Key)
    for i in range(0,10):
        if HashTable[HashValue][i].Key==-1:
            HashTable[HashValue][i]=DatatoAdd
            break
def ReadData():
    global HashTable
    File=open("HashTableData.txt")
    for Line in File:
        Data=Line.strip()
        Data=Line.split(",")
        InsertData(Record(int(Data[0]),Data[1]))
    File.close()
def GetRecord(Key):
    global HashTable
    Hashed=Hash(Key)
    for i in range(0,10):
        if HashTable[Hashed][i].Key==Key:
            return HashTable[Hashed][i].Data
    return "Not Found"
#Main
InitialiseHashTable()
ReadData()
for i in range(5):
    Key=int(input("Enter Key:"))
    print(GetRecord(Key))




