global Jobs,NumberOfJobs
Jobs=[[0]*2 for i in range(100)]
def Initialise():
    global Jobs,NumberOfJobs
    NumberOfJobs=0
    for x in range(0,100):
        Jobs[x][0]=-1
        Jobs[x][1]=-1

def AddJob(Jobnum,Priority):
    global Jobs,NumberOfJobs
    if NumberOfJobs <101:
        Jobs[NumberOfJobs][0]=Jobnum
        Jobs[NumberOfJobs][1]=Priority
        NumberOfJobs+=1
        print("Added")
    else:
        print("Not added")

def InserstionSort():
    global Jobs,NumberOfJobs
    for i in range(0,len(Jobs)):
        To_Insert=Jobs[i][0]
        To_Insert2=Jobs[i][1]
        current=i-1
        while i > 0 and Jobs[i-1][1] > To_Insert2:
            Jobs[i][0]=Jobs[i-1][0]
            Jobs[i][1]=Jobs[i-1][1]
            i-=1
        Jobs[i][0]=To_Insert
        Jobs[i][1]=To_Insert2

def PrintArray():
    global Jobs,NumberOfJobs
    for i in range(0,100):
        if Jobs[i][0] !=-1:
            print(f'{Jobs[i][0]} priority {Jobs[i][1]}')
Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
InserstionSort()
PrintArray()