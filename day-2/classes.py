class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

person = Person(15, 'Robert')
print(person.age, person.name)