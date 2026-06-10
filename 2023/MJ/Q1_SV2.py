global  Animals 
Animals=[]

Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")
def SortDecensding():
    global  Animals 
    ArrayLength=len(Animals)
    for i in range(0,ArrayLength-1):
        for x in range(0,ArrayLength-i-1):
            if (Animals[x][0])<(Animals[x+1][0]):
                Animals[x+1],Animals[x]=Animals[x],Animals[x+1]
#Main
SortDecensding()
for i in range(0,len(Animals)):
    print(Animals[i])