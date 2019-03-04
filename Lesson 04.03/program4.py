
firstDictionary = {}
anotherDictionry = dict()

firstDictionary = {"one":1, "two":2, "three" : ["kek", 3]}
print(firstDictionary["three"])

print(firstDictionary.values())

someKeys = firstDictionary.keys()
#someKeys.sort()
#for i in someKeys:
#    print(firstDictionary[i])

firstDictionary["one"] = "kek"
print(firstDictionary)
