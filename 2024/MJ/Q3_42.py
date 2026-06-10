NumberArray=[100,85,644,22,15,8,1]
def RecursiveInserstion(Array,NumberElements):
    if NumberElements<1:
        return Array
    else:
        RecursiveInserstion(Array,NumberElements-1)
        LastItem=Array[NumberElements-1]
        CheckItem=NumberElements-2
    LoopAgain=True
    if CheckItem<0:
        LoopAgain=False
    else:
        if Array[CheckItem]<LastItem:
            LoopAgain=False
    while LoopAgain:
        Array[CheckItem+1]=Array[CheckItem]
        CheckItem-=1
        if CheckItem<0:
            LoopAgain=False
        else:
            if Array[CheckItem]<LastItem:
                LoopAgain=False
    Array[CheckItem+1]=LastItem
    return Array

valval=RecursiveInserstion(NumberArray,7)
print("Recursive")
print(valval)
def ItterativeInsertion(Array):
    ArrayLen=len(Array)
    for i in range(1,ArrayLen):
        LastItem=Array[i]
        Temppointer=i
        while Temppointer>0 and Array[Temppointer-1]>LastItem:
            Array[Temppointer]=Array[Temppointer-1]
            Temppointer-=1
        Array[Temppointer]=LastItem
    return Array
print("Itterative")
returnval=ItterativeInsertion(NumberArray)
print(returnval)
def BinarySearch(IntegerArray,First,Last,ToFind):
    if First>Last:
        return -1
    else:
        Mid=(First+Last)//2
        if IntegerArray[Mid]==ToFind:
            return Mid
        elif IntegerArray[Mid]>ToFind:
            return BinarySearch(IntegerArray,First,Mid-1,ToFind)
        else:
            return BinarySearch(IntegerArray,Mid+1,Last,ToFind)
val=BinarySearch(NumberArray,0,6,644)
if val==-1:
    print("Not Found")
else:
    print(f'The number was found at index {val}')
