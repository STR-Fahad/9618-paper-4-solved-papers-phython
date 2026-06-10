global DataStored ,NumberItems
DataStored=[]# Integer array of size 20
def Initialise():
    global DataStored ,NumberItems
    placed= False
    while not placed:
        val = int(input("Enter the ammount of number u want to enter between 1 and 20: "))
        if 1<=val<=20:
            placed=True
    for i in range(0,val):
        ToAdd=int(input("Enter the number: "))
        DataStored.append(ToAdd)
        NumberItems+=1
def BubbleSort():
    global DataStored ,NumberItems
    for i in range(0,NumberItems):
        for x in range(0,NumberItems-1):
            if DataStored[x]>DataStored[x+1]:
                DataStored[x],DataStored[x+1]=DataStored[x+1],DataStored[x]
def BinaraySearch(DataToFind):
    global DataStored ,NumberItems
    max=NumberItems
    min=0
    while(min<=max):
        Mid=int((max+min)/2)
        if DataToFind==DataStored[Mid]:
            return Mid
        elif DataToFind<DataStored[Mid]:
            max=Mid-1
        else:
            min=Mid+1
    return-1

#Main
NumberItems=0
Initialise()
BubbleSort()
print("Array contents")
for i in range(0,NumberItems):
    print(DataStored[i])
Tofind=int(input("Enter the number u want to find: "))
print(BinaraySearch(Tofind))
