class Person:
    def __init__(self, name, age):
        self.firstname = name
        self.firstage = age
    
    def printname(self):
        print(self.firstname, self.firstage)
        
        
x = Person("John", "19")
x.printname()


class Student(Person):
    def __init__ (self, name, age):
        Person.__init__(self, name, age) # OR  def __init__(self, fname, lname): "/n" Person.__init__(self, fname, lname)
    


x1 = Student("Mike", "Olsen")
x1.printname()