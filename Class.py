class Cars:
    ''' A class named Cars has been created'''
    def __init__(self,company,color):
        self.company=company
        self.color=color

#inheritance:
class Cobalt(Cars):
    def __init__(self, company, color):
        super().__init__(company, color)
    def __str__(self):
        return f"Company of Cobalt: {self.company} color of Cobalt: {self.color}"
    
c1=Cobalt('Samauto','black')
c2=Cobalt('Navoiy Avto saloni','white')
c3=Cobalt('SamAuto','green')

class Kia(Cars):
    def __init__(self, company, color):
        super().__init__(company, color)
    def __str__(self):
        return f"Company of Kia: {self.company} color of Kia: {self.color}"

k1=Kia('ASACAR','black blue')
k2=Kia('UzAuto Motors Uzbekistan','rad')
k3=Kia('DUBAI','white')

class Damas(Cars):
    def __init__(self, company, color):
        super().__init__(company, color)
    def __str__(self) :
        return f"Company of Damas : {self.company} color of Damas: {self.color}"

d1=Damas('SamAuto','white')
d2=Damas('Asacar','black')
d3=Damas('NavAuto','yellow')

class Nexia(Cars):
    def __init__(self, company, color):
        super().__init__(company, color)
    def __str__(self):
        return f"company of Nexia : {self.company} color of Nexia: {self.color}"

n1=Nexia('NavAuto','green')
n2=Nexia('Dubai','yellow')
n3=Nexia('UzAuto Motors Uzbekistan','rad')

class Jetaur(Cars):
    def __init__(self, company, color):
        super().__init__(company, color)
    def __str__(self) :
        return f"company of Jetaur: {self.company} color of Jetaur: {self.color}"
    
j1=Jetaur('ASACAR','black blue')
j2=Jetaur('UzAuto Motors Uzbekistan','rad')
j3=Jetaur('DUBAI','white')

print(c1)
print(k1)
print(d1)
print(n1)
print(j1)