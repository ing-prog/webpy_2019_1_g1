name = ["Alice", "Bob"]

temp = [1,2,3,4, 4.5, 12.555, "some string", name]
#print(temp)


temp2 = list()

# MUTEX
name = ["Alice", "Bob", "Petya"]
print(name)

name[0] = "Martin"
print(name)

anotherName = "Ricarddddo"
name.append( anotherName)
print(name)

print(len(name))

numbers = [1,2,3,4,501,-2,123.2,92,-1,15]
slice1 = numbers[3:8]
print(slice1)

lastElement = numbers[-6:-1]
print(lastElement)

print(numbers)
print(numbers.sort(reverse = True))
print(numbers)


