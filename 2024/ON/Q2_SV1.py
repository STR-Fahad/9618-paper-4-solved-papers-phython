class Tree:
    def __init__(self,Ntree,Height,Max,Width,pEvergreen):
        self.TreeName=Ntree
        self.HeightGrowth=Height
        self.MaxHeight=Max
        self.MaxWitdh=Width
        self.Evergreen=pEvergreen
    def GetTreeName(self):
        return self.TreeName
    def GetGrowth(self):
        return self.HeightGrowth
    def GetMaxHeight(self):
        return self.MaxHeight
    def GetMaxWidth(self):
        return self.MaxWitdh
    def GetEvergreen(self):
        return self.Evergreen
def ReadData():
    try:
        TreeArray=[]
        File=open("Trees.txt","r")
        for i in range(0,9):
            F_line=File.readline().strip()
            name,growth,height,width,ever=F_line.split(",")
            TreeArray.append(Tree(name,int(growth),int(height),int(width),ever))
        File.close()
        return TreeArray
    except IOError:
        print("File not found")
def PrintTrees(Tree_obj):
    if Tree_obj.GetEvergreen()=="No":
        print(f'{Tree_obj.GetTreeName()} has a maximum height of {Tree_obj.GetMaxHeight()} a maximum width {Tree_obj.GetMaxWidth()} and grows {Tree_obj.GetGrowth()} cm a year. It does not lose its leaves..')
    else:
        print(f'{Tree_obj.GetTreeName()} has a maximum height of {Tree_obj.GetMaxHeight()} a maximum width {Tree_obj.GetMaxWidth()} and grows {Tree_obj.GetGrowth()} cm a year. it loses its leaves each year .')


#Main
Array=ReadData()
PrintTrees(Array[0])
