import datetime
class Character:
    def __init__(self,Charname,Dob,Int,pspeed):
        self.CharacterName=Charname
        self.DateOfBirth=Dob
        self.Intelligence=Int
        self.Speed=pspeed
    def GetName(self):
        return self.CharacterName
    def GetIntelligence(self):
        return self.Intelligence
    def SetIntelligence(self,val):
        self.Intelligence=val
    def Learn(self):
        self.Intelligence=self.Intelligence*1.1
    def ReturnAge(self):
        return 2023-self.DateOfBirth.year

FirstCharacter=Character("Royal",datetime.datetime(2019,1,1),70,30)
FirstCharacter.Learn()
print(f'The Character Name is  {FirstCharacter.GetName()} its age is {FirstCharacter.ReturnAge()}  and his intelligence is {FirstCharacter.GetIntelligence()}')

class MagicCharacter(Character):
    def __init__(self,elementp,Charname,Dob,Int,pspeed):
        self.Elemnent=elementp
        super().__init__(Charname,Dob,Int,pspeed)
    def Learn(self):
        if self.Elemnent=="fire"or self.Elemnent=="water":
            super().SetIntelligence(super().GetIntelligence()*1.2)
        elif self.Elemnent=="earth":
            super().SetIntelligence(super().GetIntelligence()*1.3)
        else:
            super().SetIntelligence(super().GetIntelligence()*0.9)

FirstMagic=MagicCharacter("fire","Light",datetime.datetime(2018,3,3),75,22)
FirstMagic.Learn()
print(f'Name is {FirstMagic.GetName()} his age {FirstMagic.ReturnAge()} and intelligence {FirstMagic.GetIntelligence()}')
