def Sum(a,b):

    return a+b


print(Sum(2,3))
print(type(Sum))

a = Sum(2,3)
b = Sum
print(a)
print(b(2,3))

############################

def Sub(a = 0,b=0):

    return a - b

print("Sub is ", Sub(2,3))
print("Sub default is ", Sub(b=1))

####################
def PrintMe(int):
    print(int)


PrintMe("Welcome!")
PrintMe(2)


#################

def Mult(x,y):
    return x*y

numerics = [1,2]
print(Mult(numerics[0], numerics[1]))
print(Mult(*numerics))

numericsDict = {"a":1, "b":3}
print(*numericsDict)

########



