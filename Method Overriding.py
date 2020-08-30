class A:

    def show(self):
        print("in a show")

class B(A):

    def show(self): # this method overrides class A show method
        print('in B show')

a1 = B()

a1.show()
