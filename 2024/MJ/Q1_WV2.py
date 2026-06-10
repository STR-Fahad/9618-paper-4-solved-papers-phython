class EventItem:
    def __init__(self,Pevent,Ptype,pdiff):
        self.EventName=Pevent
        self.Type=Ptype
        self.Difficulty=pdiff

    def GetName(self):
        return self.EventName
    def GetType(self):
        return self.Type
    def GetDifficuilty(self):
        return self.Difficulty
class Character:
    def __init__(self,Pcharactername,pjump,pswim,prun,pdrive):
        self.CharacterName=Pcharactername
        self.Jump=pjump
        self.Swim=pswim
        self.Run=prun
        self.Drive=pdrive
    def Getname(self):
        return self.CharacterName
    def CalculateScore(self,eventType,eventDiff):
        if eventType.lower()=="jump":
            winChance=self.Jump
        elif eventType.lower()=="swim":
            winChance=self.Swim
        elif eventType.lower()=="run":
            winChance=self.Run
        elif eventType.lower()=="drive":
            winChance=self.Drive
        if winChance < eventDiff:
            difference=eventDiff - winChance
            if difference == 1:
                return 80
            elif difference==2:
                return 60
            elif difference==3:
                return 40
            elif difference==4:
                return 20
        else:
            return 100




#Main
Groups=[] #Local array of Type events
Groups.append(EventItem("Bridge","Jump",3))
Groups.append(EventItem("Water wade","swim",4))
Groups.append(EventItem("100 mile run","run",5))
Groups.append(EventItem("Gridlock","drive",2))
Groups.append(EventItem("Wall on wall","jump",4))
Tarz = Character("Tarz",5,3,5,1)
Geni = Character("Geni",2,2,3,4)

score_Tarz = 0
scorre_Geni = 0

for i in range(0,5):
    PercentageTarz=Tarz.CalculateScore(Groups[i].GetType(),Groups[i].GetDifficuilty())
    PercentageGeni=Geni.CalculateScore(Groups[i].GetType(),Groups[i].GetDifficuilty())
    if PercentageGeni == PercentageTarz:
        print("It was a draw")
    elif PercentageTarz > PercentageGeni:
        score_Tarz+=1
        print("Taraz wont this event ")
    else:
        scorre_Geni+=1
        print("Geni has won the event")

if score_Tarz>scorre_Geni:
    print("Taraz has won this game")
else:
    print("Geni has won this game")