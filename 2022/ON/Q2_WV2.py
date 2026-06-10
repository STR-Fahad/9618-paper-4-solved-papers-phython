class Character:
    def __init__(self,pname,px,py):
        self.Name=pname
        self.XCordinate=px
        self.YCordinate=py
    def GetName(self):
        return self.Name
    def GetX(self):
        return self.XCordinate
    def GetY(self):
        return self.YCordinate
    def ChangePosition(self,x,y):
        self.YCordinate+=y
        self.XCordinate+=x
Characters=[] # Array of type Character
try:
    File=open("Characters.txt","r")
    for i in range(0,10):
        Name=File.readline().strip()
        x=File.readline().strip()
        y=File.readline().strip()
        Characters.append(Character(Name,int(x),int(y)))
    File.close()
except IOError:
    print("File not found")
index=-1
while index==-1:
    ToFind=input("Enter the charcter name u want to find: ")
    for i in range(10):
        temp=str(Characters[i].GetName())
        if ToFind==temp:
            index=i

to_move = input("Enter letters A, W, S or D: ")
correct = False
while not correct:
    if to_move == "A" or to_move == "W" or to_move == "S" or to_move == "D":
        correct = True
    else:
        to_move = input("Enter letters A, W, S or D: ")

if to_move =="A":
    Characters[index].ChangePosition(-1,0)
elif to_move =="W":
    Characters[index].ChangePosition(0,1)
elif to_move=="w":
    Characters[index].ChangePosition(0,-1)
else:
    Characters[index].ChangePosition(1,0)

print(f'{Characters[index].GetName()} has changed cordinated to X = {Characters[index].GetX()} and Y = {Characters[index].GetY()}')
