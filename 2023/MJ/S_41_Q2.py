class Vehicle:
    def __init__(self,Pid,Pmaxspeed,PIncreasespeed,):
        self.ID=Pid #Integer
        self.IncreaseAmount=PIncreasespeed #Integer
        self.MaxSpeed=Pmaxspeed #Integer
        self.CurrentSpeed=0 #Integer
        self.HorizontalPosition=0 #Integer
    def GetMaxSpeed(self):
        return self.MaxSpeed
    def GetCurrentSpeed(self):
        return self.CurrentSpeed
    def  GetHorizontalPosition(self):
        return self.HorizontalPosition
    def GetIncreaseAmount(self):
        return self.IncreaseAmount
    def SetCurrentSpeed(self,Cspeed):
            self.CurrentSpeed=Cspeed
    def SetHorizontalPosition(self,pos):
        self.HorizontalPosition=pos
    def IncreaseSpeed(self):
        self.CurrentSpeed+=self.IncreaseAmount
        if self.CurrentSpeed>self.MaxSpeed:
            self.CurrentSpeed=self.MaxSpeed
        self.HorizontalPosition+=self.CurrentSpeed
    def OutputCurrentPosition(self):
      print("Current position =",self.HorizontalPosition)
      print("Current speed = ", self.CurrentSpeed)
class Helicopter(Vehicle):
     def __init__(self,Pid,Pmaxspeed,PIncreasespeed,VertChangeP, MaxHeightP):
         super().__init__(Pid,Pmaxspeed,PIncreasespeed)
         self.VerticalPositon=0
         self.VerticalChange=VertChangeP
         self.MaxHeight=MaxHeightP
     def IncreaseSpeed(self):
          self.VerticalPositon+=self.VerticalChange
          if self.VerticalPositon>self.MaxHeight:
              self.VerticalPositon=self.MaxHeight
          Vehicle.SetCurrentSpeed(self, Vehicle.GetCurrentSpeed(self) +Vehicle.GetIncreaseAmount(self))
          if(Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self)):
             Vehicle.SetCurrentSpeed(self, Vehicle.GetMaxSpeed(self));
          Vehicle.SetHorizontalPosition(self, Vehicle.GetHorizontalPosition(self) +Vehicle.GetCurrentSpeed(self))
     def OutputCurrent(self):
         print("Current position = ", Vehicle.GetHorizontalPosition(self))
         print("Current speed = ", Vehicle.GetCurrentSpeed(self))
         print("Current Vertical position = ",self.VerticalPositon)
V1=Vehicle("Tiger",100,20)
H1=Helicopter("Lion",350,40,3,100)
V1.IncreaseSpeed()
V1.IncreaseSpeed()
V1.OutputCurrentPosition()
H1.IncreaseSpeed()
H1.IncreaseSpeed()
H1.OutputCurrent()