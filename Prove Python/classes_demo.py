# A Class is like an object constructor, or a "blueprint" for creating objects.
# All classes have a function called __init__(), which is always executed when 
# the class is being initiated.

# Use of the __init__() function is to assign values to object properties, or other
# operations that are necessary to do when the object is being created


class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')

print(Person.age)

print(Person.__doc__)

# ===================================================================

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
