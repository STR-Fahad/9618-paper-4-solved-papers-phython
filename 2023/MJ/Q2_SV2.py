class SaleData:
    def __init__(self,pID,pQuantity):
        self.ID=pID
        self.Quantity=pQuantity
global CircularQueue,Head,Tail,NumberOfItems

CircularQueue=[]#Queue of 5 elements of type saledata
Head=0
Tail=0
NumberOfItems=0
for i in range(0,5):
    CircularQueue.append(SaleData(" ",-1))

def Enqueue(RecordToAdd):
    global CircularQueue,Head,Tail,NumberOfItems
    if NumberOfItems==5:
        return -1
    else:
        CircularQueue[Tail]=RecordToAdd
        if Tail==4:
            Tail=0
        else:
            Tail+=1
        NumberOfItems+=1
        return 1
def Dequeue():
    global CircularQueue,Head,Tail,NumberOfItems
    returnRecord=SaleData(" ",-1)
    if NumberOfItems==0:
        return returnRecord
    else:
        returnRecord=CircularQueue[Head]
        if Head==4:
            Head=0
        else:
            Head+=1
        NumberOfItems-=1
        return returnRecord
def EnterRecord():
    ID=input("Enter product ID : ")
    Quantity=input("Enter the quantity of the item : ")
    InRecord=SaleData(ID,Quantity)
    result=Enqueue(InRecord)
    if result == 1:
        print("Stored")
    elif result == -1:
        print("Full")



EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
val=Dequeue()
if val.ID=="":
    print("Error")
else:
    print(val.ID+" ",val.Quantity)
EnterRecord()
for x in range(0,5):
    print(CircularQueue[x].ID+" "+CircularQueue[x].Quantity)
