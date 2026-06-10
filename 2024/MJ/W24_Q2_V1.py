class Horse:
    def __init__(self,PName,PHeight,PPercentage):
        self.Name=PName
        self.MaxFenceHeight=PHeight
        self.PercentageSuccess=PPercentage

    def GetName(self):
        return self.Name
    def GetMaxFenceHeight(self):
        return self.MaxFenceHeight
    def Success(self,height,risk):
        if height>self.GetMaxFenceHeight():
            return self.PercentageSuccess*0.2
        else:
            if risk==1:
                return self.MaxFenceHeight*1
            elif risk==2:
                 return self.MaxFenceHeight*0.9
            elif risk==3:
                  return self.MaxFenceHeight*0.8
            elif risk==4:
                 return self.MaxFenceHeight*0.7
            elif risk==5:
                  return self.MaxFenceHeight*0.6

               

class Fence:
    def __init__(self,PHeight,Prisk):
        self.Height=PHeight
        self.Risk=Prisk
    def GetHeight(self):
        return self.Height
    def GetRisk(self):
        return self.Risk


Horses=[]
Horses.append(Horse("Beauty",150,72))
Horses.append(Horse("Jet",160,65))
print(Horses[0].GetName())
print(Horses[1].GetName())
check = False
c1=False
height=0
risk=0
Courses=[]
for z in range(0,4):
    check = False
    while check == False:
        if height>70 or height<180:
            check=True  
        height=int(input("Enter the height of the feence between 70 cm to 180 cm : "))
    c1=False
    while c1==False:
        risk=int(input("Enter the risk of this course between 1 to 5 : "))
        if risk>=1 and risk<=5 :
            c1=True
       
    Courses.append(Fence(height,risk))
total=0
for i in range(0,2):
    for x in range(0,4):
        chance=Horses[i].Success(Courses[x].GetHeight(),Courses[x].GetRisk())
        total+=chance
    print(f'The horse {Horses[i].GetName()} has a chance of {total/4}% of jumping over all 4 fences ') 
    total=0