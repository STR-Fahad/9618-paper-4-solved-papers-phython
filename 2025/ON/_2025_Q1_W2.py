class Bird:
    def __init__(self,Pspecices,PDIstanceperh):
        self.DistancePerHour=PDIstanceperh #Real
        self.Species=Pspecices #String
        self.XPosition=500.0 #Real
        self.YPosition=500.0 #Real
    def GetSpecies(self):
        return self.Species
    def GetPosition(self):
        return (f'X = {self.XPosition} Y = {self.YPosition}')
    def Move(self,Direction,Time):
        DistanceTravel=(self.DistancePerHour/60)*Time
        if Direction=="N":
            self.YPosition+=DistanceTravel
        elif Direction=="S":
            self.YPosition-=DistanceTravel
        elif Direction=="W":
            self.XPosition-=DistanceTravel
        elif Direction=="E":
            self.XPosition+=DistanceTravel

#Main
Bird1=Bird("Cockatiel",71.0)
Bird2=Bird("Macaw",56.0)

choice=0
while choice!=1 and choice!=2:
    print("Which bird do u want to move")
    (print(f'Enter 1 for {Bird1.GetSpecies()} is currently at {Bird1.GetPosition()} or Enter 2 for {Bird2.GetSpecies()} is currently at {Bird2.GetPosition()}'))
    choice=int(input())
direction="vgbhnjmk"
while direction!="W" and direction!="E" and direction!="S" and direction!="N":
    print("Enter Which direction to move the bird use N,S,W,E : ")
    direction=input()
Time=-99
while Time<0 or Time>500:
    print("Enter the time to the nearest minute that the bird has been travelling")
    Time=int(input())
if choice==1:
        Bird1.Move(direction,Time)
else:
    Bird2.Move(direction,Time)

print(f'The new postion of {Bird1.GetSpecies()} is {Bird1.GetPosition()}')
print(f'The new postion of {Bird2.GetSpecies()} is {Bird2.GetPosition()}')
