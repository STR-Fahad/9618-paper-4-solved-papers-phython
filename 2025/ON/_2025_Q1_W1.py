import random
global TopofStack
TopofStack=-1
Stack=[""]*30
def Push(Val):
    global TopofStack
    if TopofStack>=29:
        return False
    elif TopofStack==-1:
        TopofStack=0
        Stack[TopofStack]=Val
        
        return True
    else:
        TopofStack+=1
        Stack[TopofStack]=Val
        
        return True
    
def Pop():
    global TopofStack
    if TopofStack==-1:
        return -999
    else:
        Value=Stack[TopofStack]
        TopofStack-=1
        return Value
def FindValues():
    Largest=-999999
    Smallest=9999999
    Temp=0
    for i in range(0,30):
        Temp=Pop()
        if Temp>Largest:
            Largest=Temp
        elif Temp<Smallest:
            Smallest=Temp
    print(f'The Largest value in the stack is : {Largest}')
    print(f'The smallest value in the stack is : {Smallest}')

#Main
for i in range(0,40):
    Random=random.randint(0,1000)
    Check=Push(Random)
    if Check==False:
        print("Stack Full")
        break
FindValues()