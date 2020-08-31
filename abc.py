class computer:

    def config(self):
        print("i5, 8gb, 1200gb")

com1 = computer() #defining object
com2 = computer() #defining object

computer.config(com1) #calling method
computer.config(com2) #calling method

com1.config() #calling method
com2.config() #calling method
