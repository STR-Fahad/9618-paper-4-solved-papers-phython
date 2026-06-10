// start
global Stack
Stack=[]
TopOfStack=-1
for i in range(0,20):
    Stack.append("-1")

def Push(Data):
    global Stack,TopOfStack
    if TopOfStack==19:
        return -1
    else:
        TopOfStack+=1
        Stack[TopOfStack]=Data
        return 1
def Pop():
    global Stack,TopOfStack
    if TopOfStack==-1:
        return -1
    else:
        Returnval=Stack[TopOfStack]
        TopOfStack-=1
        return Returnval
def ReadData(F_Name):
    global Stack,TopOfStack
    try:
        File=open(F_Name,"r")
        for Line in File:
            Returnval=Push(Line.strip())
            if Returnval==-1:
                return "Stack is full"
        File.close()
    except:
        print("File cannot be found")
def Calculate():
    global Stack,TopOfStack
    Total=Pop()
    Total=int(Total)
    Return=0
    LastOperator=""
    Operator=True
    while Return!=-1:
        Return=Pop()
        if Operator == False:
             Data = int(Return)
            if LastOperator == "+":
                  Total = Total + Data
            elif LastOperator == "-":
                 Total = Total - Data
            elif LastOperator == "*":
             Total = Total * Data
            elif LastOperator == "/":
                 Total = Total / Data
            elif LastOperator == "^":
                 Total = Total ** Data
            Operator = True
        else:
                LastOperator = Return
                Operator = False
     return Total
