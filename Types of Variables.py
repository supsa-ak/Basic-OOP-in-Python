class Car:

    wheels = 4 #class variable/static variable

    def __init__(self):                   
        self.mil = 10 # predefined attribute
        self.com = "BMW" # predefined attribute

 # Here mil and com are instance variable
 # wheels is class variable

c1 = Car()
c2 = Car()

c1.mil = 9
#c1.wheels = 5 #changes for only c1
Car.wheels = 6 #changes for all objects

print(c1.mil, c2.mil, c1.wheels)
print(c1.com, c2.com, c2.wheels)
