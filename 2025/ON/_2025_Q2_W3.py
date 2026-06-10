global Queue
global QueueHead
global QueueTail
Queue=[""]*100
QueueTail=-1
QueueHead=-1
NumberItems=0
def Enqueue(DatatoInsert):
    global Queue, QueueHead, QueueTail, NumberItems
    if QueueHead==-1:
        Queue[0]=DatatoInsert
        QueueHead = 0
        QueueTail = 0
        NumberItems +=1
        return True
    elif  QueueTail>=99:
     
        Queue[QueueTail+1] = DatatoInsert
        QueueTail +=1
        NumberItems +=1
        return True
    else:
         return False

def Dequeue():
    global Queue, QueueHead, QueueTail, NumberItems
    if NumberItems==0:
        return "False"
    else:
        returnval=Queue[QueueHead]
        QueueHead+=1
        NumberItems-=1
        return returnval
def ReadData():
