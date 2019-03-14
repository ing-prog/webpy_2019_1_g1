def Something(a,b):
    return a+b/(a-b)**2


a1 = lambda a=1,b=2 : a+b/(a-b)**2
print(a1())
print(Something(2,3))


p = []
for x in range(0,1000):
    if x%2 == 0:
        p.append(x)

#print(p)



########
p1 = [x for x in range(0,1000) if x%2 ==0]
print(p1)