class Node:
    def __init__(self,pdata,pnextnode):
        self.data=pdata
        self.nextNode=pnextnode

LinkedList=[Node(1,1),Node(5,4),Node(6,7),Node(7,-1),Node(2,2),Node(0,6),Node(0,8),Node(56,3),Node(0,9),Node(0,-1)]
Startpointer=0
emptylist=5
def OutputNodes(LinkedList,currentpointer):
    while (currentpointer !=-1):
        print(str(LinkedList[currentpointer].data))
        currentpointer=LinkedList[currentpointer].nextNode

OutputNodes(LinkedList,Startpointer)
def addNode(LinkedList,startpointer,emptylist):
    ToAdd=int(input("enter the data u want to add"))
    if emptylist<=0 or emptylist>9:
        return False
    else:
        newNode=Node(ToAdd,-1)
        LinkedList[emptylist]=newNode
        previous=0
        while startpointer != -1:
            previous=startpointer
            startpointer =LinkedList[startpointer].nextNode
        LinkedList[previous].nextNode=emptylist
        emptylist=LinkedList[emptylist].nextNode
        return True
val=addNode(LinkedList,Startpointer,emptylist)
if val ==True:
    print("The node was added")
else:
    print("The node was not added")
OutputNodes(LinkedList,Startpointer)