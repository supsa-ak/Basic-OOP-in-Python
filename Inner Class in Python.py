class Student: #outer class

    def __init__(self):
        self.name = "sak" # predefined variable
        self.rollno = 8 # predefined variable
       #self.config = self.Laptop()
       #print(self)

    class Laptop: # inner class

        def __init__(g):
            g.brand = 'HP' # predefined variable
            g.cpu = "i7" # predefined variable
            g.ram = '8gb' # predefined variable
            #print(g.brand, g.cpu, g.ram)
           #print(g)

s1 = Student()
lap1 = Student.Laptop() # defining object out of outer class
print(lap1.ram)

#print(s1.name, s1.rollno)

#print(s1.config.brand)
