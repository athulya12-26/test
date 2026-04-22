class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private property

p1 = Person("anu",20)
print(p1.name)
print(p1._Person__age)