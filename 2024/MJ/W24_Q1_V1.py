
def ReadData():
    Arr=[]
    File=open("Data.txt","r")
    for i in range(0,45):
        F_line=File.readline().strip()
        Arr.append(F_line)
    return Arr
def FormatArray(array):
    word=array[0]+" "
    for i in range(1,45):
        word=word+" "+array[i]
    print(word)
def CompareString(s1,s2):
   for i in range(0,len(s1)):
       if s1[i]>s2[i]:
           return 2
       elif s1[i]<s2[i]:
           return 1
def Bubblesort(array):
    for i in range(0,len(array)-1):
        for y in range(0, len(array) - i - 1):
            returnval=CompareString(array[y],array[y+1])
            if returnval==2:
               array[y],array[y+1]=array[y+1],array[y]
    return array


Array=ReadData()
FormatArray(Array)
arr=Bubblesort(Array)
FormatArray(arr)