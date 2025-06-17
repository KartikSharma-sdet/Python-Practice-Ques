import Input_Keywords.input as input

class Car:
    followers = 0
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def displayName(self):
        print(self.name)

    def editName(self, newName):
        self.name = newName

car1 = Car("Tata", "Delhi")
car1.displayName()
car1.editName("Mercedes")
car1.displayName()

class sedan(Car):
    tyres = 4
    color = ""
    mechanism = ""

    def setColor(self, color):
        self.color = color

    def setMechanism(self, mech):
        self.mechanism = mech

hondaCity = sedan("HondaCity", "Delhi")

hondaCity.setColor("White")
hondaCity.setMechanism("Automatic")

print(hondaCity.color, hondaCity.name)