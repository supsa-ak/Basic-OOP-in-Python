class Computer:

    def __init__(self):
        self.name = "sak" # predefine parameter
        self.age = 19 # predefine parameter
        # here name and age are variables

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print('They are same.')
