class Figure:
    def __init__(self, c = "green", w = 10, l = 10):
        self.__color = c
        self.__width = w
        self.__length = l
        print('COnstruct DOne!')

    def getSquare(self):
        return self.__width*self.__length
    
    def setWidth(self, width):
        self.__width = width
    def setLength(self, length):
        self.__length = length

    def __getSquare(self):
        return self.__width*self.__length


fig = Figure()
print( fig.getSquare())

fig.setLength(50)
fig.setWidth(50)
print( fig.getSquare())

