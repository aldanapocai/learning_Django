#Python Framework
#ORM -> Object Relating Mapping

class Person:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

#Default constructor = static data
#Constructor = parameters

    def setschool(self, school):
        self.school = school

    def getschool(self):
        return self.school

    def descr(self):
        print("My name is ", self.name)
        print("My age is", self.age)
        

#Creating an object of the class

demo_person = Person('Tomi', 13)
demo_person2 = Person('Aldi', 26)

# print(demo_person.name)

# demo_person.descr()
# demo_person2.descr()

demo_person.setschool('Oxford')

print(demo_person.getschool())