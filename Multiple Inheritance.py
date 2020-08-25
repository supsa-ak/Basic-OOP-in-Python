# Single level inheritance
class A: # Parent class / super class
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
a1 = A()

a1.feature1()
a1.feature2()

class B: # child class / sub class
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

b1 = B()

b1.feature3()
b1.feature4()


class C(A,B): # child class / sub class
    def feature5(self):
        print("Feature 5 is working")
    def feature6(self):
        print("Feature 6 is working")

c1 = C()

c1.feature5()
c1.feature6()
c1.feature3()
c1.feature4()
c1.feature1()
c1.feature2()
