class Omacka:


    def __init__(self):
        self.__voda = 0
        self.__mouka = 0
    
    @property
    def voda(self):
        return self.__voda
    
    @property
    def mouka(self):
        return self.__mouka
    
    @mouka.setter
    def mouka(self, value):
        if value >= 0:
            self.__mouka = value
    





    
    def serviruj(self):
        if (self.voda > self.mouka):
            return "Omáčka"
        else:
            return "Fuj"
        
    def pridej_mouku(self, kolik):
        if (self.voda > self.mouka + kolik):
            self.mouka += kolik

omacka = Omacka()
print(omacka.voda)

omacka.mouka=100
omacka.voda=50

print(omacka.serviruj())