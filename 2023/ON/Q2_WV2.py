def IterativeCalculate(num):
    ToFind=num
    Total=0
    while num!=0:
        if (ToFind%num)==0:
            Total+=num
        num-=1
    return Total
def RecursiveValue(num,Tofind):
    if num==0:
        return 0
    else:
        if Tofind%num==0:
            return num+RecursiveValue(num-1,Tofind)
        else:
            return  RecursiveValue(num-1,Tofind)
y=RecursiveValue(50,50)
print(y)
x=IterativeCalculate(10)
print(x)