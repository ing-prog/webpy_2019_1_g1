line = list()

class Rectangle:

    def __init__(self, w= 1, l = 1):
        print("Construct Working!!")
        self.width = w
        self.length = l

    def __del__(self):
        print("Destructor WOrking!")


fig = Rectangle()




print(fig.width, fig.length)


