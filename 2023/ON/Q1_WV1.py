
def ItterativeVowel(Value):
    Total=0
    LengthString=len(Value)
    for i in range(0,LengthString):
        FirstCharacter=Value[0]
        if FirstCharacter=="a" or FirstCharacter=="e" or FirstCharacter=="i" or FirstCharacter=="o" or FirstCharacter=="u":
            Total+=1
        Value=Value[1:len(Value)]
    return Total
def RecursiveVowel(Value):
    if len(Value)==0:
        return 0
    else:
        FirstCharacter=Value[0]
        if FirstCharacter=="a" or FirstCharacter=="e" or FirstCharacter=="i" or FirstCharacter=="o" or FirstCharacter=="u":
            return 1+RecursiveVowel(Value[1:len(Value)])
        else:
            return RecursiveVowel(Value[1:len(Value)])





print(RecursiveVowel("imagine"))
print(ItterativeVowel("house"))