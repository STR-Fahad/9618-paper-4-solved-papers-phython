global DataArray
DataArray=[]#Array of size 100
def ReadFile():
    global DataArray
    try:
        File=open("IntegerData.txt","r")
        correct=False
        while not correct:
            F_line=File.readline().strip()
            if F_line=="":
                correct=True
            else:
                DataArray.append(int(F_line))

    except IOError:
        print("File not found")
def FindValues():
    global DataArray
    lfile=len(DataArray)
    tofind=int(input("Enter the number u want to find between 1 to 100 : "))
    count=0
    for i in range(0,lfile):
        if DataArray[i]==tofind:
            count+=1
    return count
def BubbleSort():
    global DataArray
    for i in range(0,100):
        for x in range(0,99):
            if DataArray[x]>DataArray[x+1]:
                DataArray[x],DataArray[x+1]=DataArray[x+1],DataArray[x]
#Main
ReadFile()
val=FindValues()
print("The number of time the number appeared is ", val)
BubbleSort()
print(DataArray)