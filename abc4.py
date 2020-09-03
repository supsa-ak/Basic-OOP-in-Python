class Computer:

    def __init__(self):
        self.name = "sak" # predefine parameter
        self.age = 19 # predefine parameter
        # here name and age are variables

    def update(self):
            self.age = 20

c1 = Computer()
c2 = Computer()

c1.name = "pak" # passing value to attribute outside calling object
c2.age = 12

#c2.update()
Computer.update(c2)
#c2.update()

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)
