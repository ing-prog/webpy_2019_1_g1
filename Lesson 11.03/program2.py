def PrintStr(temp):
    print(temp)

def Mult(x,y):
    return x*y

funcList = [PrintStr, Mult]

funcList[0]("LOl")

newDict = {PrintStr:"LOl", Mult:"Qwerty"}
print(newDict[PrintStr])




def PrintFunc(abcd):
    abcd("Kek")

PrintFunc(PrintStr)


