global TreeArray
global RootPointer
global FreeNode
RootPointer=-1
FreeNode=0
TreeArray=[]
for i in range(0,50):
    TreeArray.append([-1,-1,-1])

def AddNode(ToAdd):
    global TreeArray
    global RootPointer
    global FreeNode
    if FreeNode<=49:
        TreeArray[FreeNode][0]=-1
        TreeArray[FreeNode][1]=ToAdd
        TreeArray[FreeNode][2]=-1
        if RootPointer == -1:
             RootPointer = FreeNode
             FreeNode += 1
        else:
            Placed=False
            CurrentNode=RootPointer
            while Placed==False:
                if ToAdd <TreeArray[CurrentNode][1]:
                    if TreeArray[CurrentNode][0]==-1:
                        TreeArray[CurrentNode][0]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=TreeArray[CurrentNode][0]
                else:
                    if TreeArray[CurrentNode][2]==-1:
                        TreeArray[CurrentNode][2]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=TreeArray[CurrentNode][2]
            FreeNode+=1
    else:
        print("The tree is full")
def WriteALlToFile():
    try:
        File=open("Tree.txt","w")
        for i in range(0,50):
            line = f"{TreeArray[i][0]},{TreeArray[i][1]},{TreeArray[i][2]}\n"
            File.write(line)
        File.close()
    except:
        print("Cannot write file")

#Main
try:
 File= open("TreeData.txt")
 for Line in File:
    AddNode(int(Line.strip()))
 File.close()
except:
 print("Error cannot open file")
WriteALlToFile()