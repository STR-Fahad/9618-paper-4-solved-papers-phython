global StackVowel,VowelTop,ConstantTop,StackConstant
StackVowel=[]
StackConstant=[]
ConstantTop=0
VowelTop=0
def PushData(ToPush):
    global StackVowel,VowelTop,ConstantTop,StackConstant
    ToPush=ToPush.lower()
    if ToPush=="a"or ToPush=="e"or ToPush=="i" or ToPush=="o" or ToPush=="u":
        if VowelTop>=100:
            print("Vowel stack is full")
        else:
            StackVowel.append(ToPush)
            VowelTop+=1
    else:
        if ConstantTop>=100:
            print("COnstant stack is full")
        else:
            StackConstant.append(ToPush)
            ConstantTop+=1
def ReadData():
    global StackVowel,VowelTop,ConstantTop,StackConstant
    try:
        File=open("StackData.txt","r")
        for i in range(0,100):
            F_Line=File.readline().strip()
            PushData(F_Line)
    except IOError:
        print("File not found")
def PopConstant():
    global StackVowel,VowelTop,ConstantTop,StackConstant
    if ConstantTop==0:
        return "No Data"
    else:
        ConstantTop-=1
        returndata=StackConstant[ConstantTop]
        ConstantTop-=1
        return returndata
def PopVowel():
    global StackVowel,VowelTop,ConstantTop,StackConstant
    if VowelTop==0:
        return "No Data"
    else:
        VowelTop-=1
        returndata=StackVowel[VowelTop]
        VowelTop-=1
        return returndata
ReadData()
count=0
outstring=""
while count!=5:
    inputdata=input("Enter ur choice of a vowel or constant : ")
    if inputdata=="vowel":
        data=PopVowel()
        if data!="No Data":
            outstring=outstring+data
            count+=1
        else:
            print("The stack was empty")
    else:
        data=PopConstant()
        if data!="No Data":
            outstring=outstring+data
            count+=1
        else:
            print("The stack was empty")

print(outstring)
