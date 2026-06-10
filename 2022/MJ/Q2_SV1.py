from re import A


global ArrayData
ArrayData=[10 ,5 ,6, 7 ,1 ,12 ,13 ,15 ,21,8]

def LinearSearch(ToFind):
    global ArrayData
    for i in range(0,10):
        if ArrayData[i]==ToFind:
            return True
    return False
def BubbleSort():
    global ArrayData
    for i in range(0,10):
        for x in range(0,9):
            if ArrayData[x]<ArrayData[x+1]:
                temp=ArrayData[x]
                ArrayData[x]=ArrayData[x+1]
                ArrayData[x+1]=temp
#Main
val=int(input("Enter the data u want to find : "))
check=LinearSearch(val)
if check==True:
    print("The data was found")
else:
    print("The data was not found")

BubbleSort()
print(ArrayData)