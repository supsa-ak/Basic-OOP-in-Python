#class
class BestCourse:  #class name

  website = 'http://www.sak.com'

  def __init__(self, name): #method #parameter/argument
    self.name = name #attribute

  
#Object
python_course = BestCourse("Learn Python")
learn_command_line_course = BestCourse("Learn command line")

print(python_course.name)
print(BestCourse.website)

print(learn_command_line_course.name) # object_name.Method
print(BestCourse.website) # Class_name.Method
