class Student:  # outer class

    def __init__(self):
        self.name = "sak"
        self.lap = self.Laptop() # defining object inside outer class

    class Laptop: # inner class

        def __init__(g):
            g.brand = "hp" # here g is s1.lap

s1 = Student()

print(s1.name)

print(s1.lap.brand)

#Lap1 = s1.lap # defining another objectname no need bullshit
#print(Lap1.brand)
