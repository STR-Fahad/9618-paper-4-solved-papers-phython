from re import L


class Node:
    def __init__(self,Dat):
        self.LeftPointer=-1
        self.Data=Dat
        self.RightPointer=-1
    def GetLeft(self):
        return self.LeftPointer
    def GetData(self):
        return self.Data
    def GetRight(self):
        return self.RightPointer
    def SetRight(self,val):
        self.RightPointer=val
    def SetData(self,val):
        self.Data=val
    def SetLeft(self,val):
        self.LeftPointer=val
class TreeClass:
    def __init__(self):
        self.FirstNode=-1
        self.NumberNode=0
        self.Tree=[]
        for i in range(0,20):
            self.Tree.append(-1)
    def InsertNode(self,NewNode):
        if self.NumberNode<=19:
            self.Tree[self.NumberNode]=NewNode
            if self.FirstNode==-1:
               self.FirstNode=0
            else:
                placed=False
                currentpointer=self.FirstNode
                while not placed:
                    if NewNode.GetData() < self.Tree[currentpointer].GetData():
                        if self.Tree[currentpointer].GetLeft()==-1:
                            self.Tree[currentpointer].SetLeft(self.NumberNode)
                            placed=True
                        else:
                            currentpointer=self.Tree[currentpointer].GetLeft()
                    else:
                        if self.Tree[currentpointer].GetRight()==-1:
                            self.Tree[currentpointer].SetRight(self.NumberNode)
                            placed=True
                        else:
                            currentpointer=self.Tree[currentpointer].GetRight()
            self.NumberNode+=1
        else:
            print("tree is full")
    def OutputTree(self):
        for x in range(0,self.NumberNode):
            print(self.Tree[x].GetLeft()," ",self.Tree[x].GetData()," ",self.Tree[x].GetRight())
         

TheTree=TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()
