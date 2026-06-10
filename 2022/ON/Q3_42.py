global Queue,HeadPointer,TailPointer
Queue=[]
TailPointer=0
HeadPointer=0

def Enqueue(ToAdd):
    global Queue,HeadPointer,TailPointer
    if TailPointer>100:
        return False
    else:
        Queue.append(ToAdd)
        TailPointer+=1
        return True
def RecursiveOutput(Start):
    global Queue,HeadPointer,TailPointer
    if Start==0:
        return Queue[Start]
    else:
        return (Queue[Start]+RecursiveOutput(Start-1))
#Main
for i in range(1,21):
    val=Enqueue(i)
if val== True:
        print("Successfull")
else:
        print("unsuccessfull")

returnval=RecursiveOutput(TailPointer-1)
print(returnval)
