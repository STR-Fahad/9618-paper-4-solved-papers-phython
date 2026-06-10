global  Animal,Colour,AnimalTopPointer,ColourTopPointer
Animal=[]
Colour=[]
ColourTopPointer=0
AnimalTopPointer=0
def PushAnimal(DataToPush):
    global  Animal,Colour,AnimalTopPointer,ColourTopPointer
    if AnimalTopPointer==20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer+=1
        return True
def PopAnimal():
    global  Animal,Colour,AnimalTopPointer,ColourTopPointer
    if AnimalTopPointer==0:
        return ""
    else:
        Data=Animal[AnimalTopPointer-1]
        AnimalTopPointer-=1
        return Data
def PopColour():
    global  Animal,Colour,AnimalTopPointer,ColourTopPointer
    if ColourTopPointer==0:
        return ""
    else:
        returnData=Colour[ColourTopPointer-1]
        ColourTopPointer-=1
        return returnData
def ReadData():
    try:
        FileColour=open("ColourData.txt","r")
        FileAnimal=open("AnimalData.txt","r")
        FColour_Line=FileColour.readline().strip()
        F_line=FileAnimal.readline().strip()
        while F_line!="":
            PushAnimal(str(F_line))
            F_line=FileAnimal.readline().strip()
            
        while FColour_Line !="":
            PushColour(FColour_Line)
            FColour_Line=FileColour.readline().strip()
            
        FileColour.close()
        FileAnimal.close()
    except IOError:
        print("FIle not found ")
def PushColour(DataToPush):
    global  Animal,Colour,AnimalTopPointer,ColourTopPointer
    if ColourTopPointer==10:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer+=1
        return True


def OutputItem():
    Cpop=PopColour()
    Apop=PopAnimal()
    if Cpop=="":
        PushAnimal(Apop)
        print("No Colour")
    elif Apop=="":
        PushColour(Cpop)
        print("No Animal")
    else:
        print(Cpop+" ",Apop)

#Main
ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
print(Animal)