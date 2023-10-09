
class Car():

    def __int__(self):
        print("This Is Constructor")
        #This id for Testgit

    def __init__(self,color):
        print("this is car class constructor")
        self.color=color

    def setPrice(self,price):
        self.price=price

    def getprice(self):
        return self.price


c1=Car("Polar While")
print(c1.color)
c1.setPrice(1000000)
print(c1.getprice())








