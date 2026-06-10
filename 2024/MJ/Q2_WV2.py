class Queue:
    def __init__(self,phead,ptail):
        self.Queue=[]
        self.HeadPointer=phead
        self.Tailpointer=ptail
        for i in range(0,100):
            self.Queue.append(-1)

TheQueue=Queue(-1,0)
def Enqueue(TheData):
    global TheQueue
    if TheQueue.HeadPointer==-1:
        TheQueue.Queue[TheQueue.Tailpointer]=TheData
        TheQueue.HeadPointer=0
        TheQueue.Tailpointer+=1
        return 1
    elif TheQueue.Tailpointer>99:
        return -1
    else:
        TheQueue.Queue[TheQueue.Tailpointer]=TheData
        TheQueue.Tailpointer+=1
        return 1
def ReturnAllData():
    global TheQueue
    Outstr=""
    for i in range(TheQueue.HeadPointer,TheQueue.Tailpointer):
        Outstr=Outstr+str(TheQueue.Queue[i])+" "
    return Outstr
def Dequeue():
    global TheQueue
    if TheQueue.HeadPointer== -1:
        return -1
    elif TheQueue.HeadPointer == TheQueue.Tailpointer:
        return -1
    else:
        theData = TheQueue.Queue[TheQueue.HeadPointer]
        TheQueue.HeadPointer+= 1
        return theData
for x in range(10):
    dataToAdd = int(input("Enter a number greater than 0: "))
    while dataToAdd < 0:
        dataToAdd = int(input("Enter a number greater than 0: "))
    success = Enqueue(dataToAdd)
    if success == -1:
        print("The queue is full")
    else:
        print("Enqueue was successful")
print(ReturnAllData())
result = Dequeue()
if result == -1:
    print("Queue empty")
else:
    print(result)
    
result = Dequeue()
if result == -1:
    print("Queue empty")
else:
    print(result)

print(ReturnAllData())