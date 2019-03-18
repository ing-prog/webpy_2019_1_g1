class Auto:
    def __init__(self, c = "yellow"):
        print("Construct Working for Auto! ")
        self.color = c
        

    def get_color(self):
        return self.color

    def info(self):
        print("Auto Info")
        print(self.color)


class Machine(Auto):
    def __init__(self, color, mph = 200, nWheels = 2):
        print("Construct Working for Machine!")
        super().__init__(color)
        self.mph = mph
        self.wheels = nWheels

    def info(self):
        print("Machine Info")
        print(self.color)
        print(self.mph)
        print(self.wheels)

    


bmw = Machine( "black", 500,  5)
djiga = Auto()

djiga.info()
bmw.info()

