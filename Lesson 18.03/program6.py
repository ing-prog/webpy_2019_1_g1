name = "Dorek"

class MyString(str):
    
    def errorPub(self, position = 1, letter = "A"):
        return   self[:position] + letter + self[position+1:]
    def getWord(self):
        return self

word = MyString(name)
word = word.errorPub()
print(word)
