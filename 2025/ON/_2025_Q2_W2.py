import random

def PrintArray(Array):
    Output=""
    for i in range(0,len(Array)):
        Output=Output+" "+str(Array[i])
    print(Output)

def BubbleSort(Array):
    for i in range(0,len(Array)):
        for x in range(0,len(Array)-1):
            if Array[x]>Array[x+1]:
                temp=Array[x]
                Array[x]=Array[x+1]
                Array[x+1]=temp
    return Array
def RecurssiveBinarySearch(Array,Lbound,Ubound,TOfind):
    if Ubound>=Lbound:
        mid=(Ubound+Lbound)//2
        if Array[mid]==TOfind:
            return mid
        elif Array[mid]>TOfind:
            return RecurssiveBinarySearch(Array,Lbound,mid-1,TOfind)
        else:
            return RecurssiveBinarySearch(Array,mid+1,Ubound,TOfind)
    else:
        return -1

#Main
Data=[""]*20
for i in range (0,20):
    Data[i]=random.randint(0,100)


PrintArray(Data)
BubbleSort(Data)
print("Sorted")
PrintArray(Data)

Value=int(input("Enter the value u want to find : "))
check=RecurssiveBinarySearch(Data,0,19,Value)
if check==-1:
    print("Not Found")
else:
    print("Found at index : ",check)