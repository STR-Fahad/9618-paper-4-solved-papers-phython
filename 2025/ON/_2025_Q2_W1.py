class Train:
    def __init__(self,PTrainNum,PRoute):
        self.TrainIDNumber=PTrainNum #String
        self.Route=PRoute #Integer
    def GetTrainIDNumber(self):
        return self.TrainIDNumber
    def GetRoute(self):
        return self.Route
class Station:
    def __init__(self,PStationid,Pnumberplatform):
        self.StationID=PStationid #String
        self.NumberPlatforms=Pnumberplatform #Integer
        self.Trains=[] #Array of 9 elements of type train
        self.NumberTrains=0 #Integer
    def AddTrain(self,NewTrain):
        if self.NumberTrains>=self.NumberPlatforms:
            return False
        else:
            self.Trains.append(NewTrain)
            self.NumberTrains+=1
            return True
    def GetTrains(self):
        if self.NumberTrains==0:
            return print("There are no Trains avaliable ")
        else:
            OutputLine= "The trains at station"+ self.StationID+ "are: \n"
            for i in range(self.NumberTrains):
                OutputLine=OutputLine+ self.Trains[i].GetTrainIDNumber()+ "are on route no  " + str(self.Trains[i].GetRoute())+ "\n"
            return OutputLine

#Main
Train1=Train("12ADV",134)
Train2=Train("33ART",20)
Train3=Train("9FKF",3)
Train4=Train("21VBC",24)#
SouthStation=Station("STH",2)
NorthStation=Station("NTH",1)
Notaccepted="Station is full"
ReturnVal1=SouthStation.AddTrain(Train1)
if ReturnVal1==False:
    print(Notaccepted)
ReturnVal2=SouthStation.AddTrain(Train2)
if ReturnVal2==False:
    print(Notaccepted)
ReturnVal3=SouthStation.AddTrain(Train2)
if ReturnVal3==False:
    print(Notaccepted)
ReturnVal4=NorthStation.AddTrain(Train4)
if ReturnVal4==False:
    print(Notaccepted)
print(SouthStation.GetTrains())
print(NorthStation.GetTrains())