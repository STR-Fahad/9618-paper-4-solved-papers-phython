DataArray=[]
def PrintArray(Array):
    word=""
    for i in range(len(Array)):
        word=word+" "+str(DataArray[i])
    print(word)
def LinearSearch(Array,Val):
    count=0
    for i in range(0,len(Array)):
        if Array[i]==Val:
            count+=1
    return count
try:
    File=open("Data.txt","r")
    for i in range(0,25):
        F_line=File.readline().strip()
        DataArray.append(int(F_line))
    File.close()
except IOError:
    print("File not found")

Tofind=-1
check=False
while check!=True:
    if Tofind>=0 and Tofind<=100:
        check=True
        break
    Tofind=int(input("Enter a number u want to find between 0 and 100: "))
returnval=LinearSearch(DataArray,Tofind)
print(f'The number {Tofind} was found {returnval}  times ')
