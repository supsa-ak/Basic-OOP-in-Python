class computer:

    def __init__(self):
        print("in init")

    def job(self):
        print("got")

    def config(self):
        print("i5, 8gb, 1200gb")

com1 = computer() #defining object/calling class
com2 = computer() #defining object/calling class

com1.config() #calling method
com2.config() #calling method

com1.job()
com2.job()

#everything is called separately in output
#6 output has 6 callings one by one as called
#he say above right that check it carefully
