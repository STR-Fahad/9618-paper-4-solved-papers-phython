
global NumberWords , WordArray
WordArray=[]
NumberWords=0
def ReadData(FName):
    global NumberWords , WordArray
    try:
        File=open(FName,"r")
        f_Line=File.readline().strip()
        while f_Line!="":
            WordArray.append(f_Line)
            NumberWords+=1
            f_Line=File.readline().strip()
        File.close()
        Play()
    except IOError:
        print("File not found")
def Play():
    global NumberWords , WordArray   
    print("The main word is : ",WordArray[0])
    User_Dat=input("Enter ur answer: ")
    Correct=0
    while User_Dat!="no":
        count=0
        sucess=False
        while not sucess and count<len(WordArray):
            for i in range(1,len(WordArray)):
                if User_Dat==WordArray[i]:
                    print("Its an answer")
                    WordArray[i]=""
                    Correct+=1
                    User_Dat=input("Enter ur answer: ")
                    sucess=True
                    break
            count+=1
        if not sucess:
            print("This is not an answer")
            User_Dat=input("Enter ur answer: ")
    percencorrect=int((Correct/NumberWords)*100)
    print("The percentange of correct answers are ",percencorrect)
    for x in range(len(WordArray)):
     if WordArray[x]!="":
        print(WordArray[x])



        
#Main
FName=input("Enter which level u want to play : ")
if FName=="easy":
    ReadData("Easy.txt")
elif FName=="hard":
    ReadData("Hard.txt")
elif FName=="medium":
     ReadData("Medium.txt")
else:
    print("Invalid input ")
