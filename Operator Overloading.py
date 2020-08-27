class Student:

    def __init__(self, j1, j2):
        self.m1 = j1
        self.m2 = j2

    def __add__(self, o): # here __add__ is also special type of method it is called by calling class like __init__
        m1 = self.m1 + o.m1
        m2 = self.m2 + o.m2
     #   s3: Student = Student(m1, m2)
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2 :
            return  True
        else :
            return False
    def __str__(self):
        return '{} {}'.format(self.m1 , self.m2)

sak = Student(60, 100)
pak = Student(60, 90 )

s3 = sak + pak # we want to add m1 of both objects and m2 of both objects

print(s3.m1)
print(s3.m2)


if sak > pak :
    print('sak wins')
else:
    print("pak wins")

print(sak)
#print(sak.__str__())
print(pak)
