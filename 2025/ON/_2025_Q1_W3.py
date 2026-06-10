class BoardObject:
    def __init__(self,Pcode,Pvalue):
        self.Code=Pcode
        self.Value=Pvalue

    def GetCode(self):
        return self.Code
    def GetValue(self):
        return self.Value

class Board:
    def __init__(self):
        self.TheBoard=[]
        for x in range(10):
            TempList = []
            for y in range(10):
                 TempList.append(BoardObject("-",0))
            self.TheBoard.append(TempList)
    def GetObject(self,Rowno,Colno):
        return self.TheBoard[Rowno][Colno]
    def SetObject(self,Object,Rowno,Colno):
        self.TheBoard[Rowno][Colno]=Object
    def DisplayBoard(self):
        for i in range(10):
            Outputline=""
            for x in range(10):
                Outputline=Outputline+str(self.TheBoard[i][x].GetCode())+" "
            print(Outputline)

        
#Main
GameBoard=Board()
Object1=BoardObject("A",2)
Object2=BoardObject("B",3)
Object3=BoardObject("C",5)
Object4=BoardObject("D",2)
Object5=BoardObject("E",7)
GameBoard.SetObject(Object1, 0, 0)
GameBoard.SetObject(Object2, 9, 9)
GameBoard.SetObject(Object3, 4, 5)
GameBoard.SetObject(Object4, 2, 2)
GameBoard.SetObject(Object5, 8, 7)
GameBoard.DisplayBoard()