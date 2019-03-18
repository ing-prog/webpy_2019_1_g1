class Figure:
    kek = 10
    _lol = 20
    __pep = 3000

    def getPep(self):
        return self.__pep

fig = Figure()
print(fig.kek)
print(fig._lol)

fig._lol = 999999
print(fig._lol)

#print(fig.__pep)
print(fig.getPep())
    
   


    

    