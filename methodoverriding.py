class Animal:
    def make_sound(self):
        return "Some generic animal sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
a = Animal()
d = Dog()
c = Cat()
print(a.make_sound())  
print(d.make_sound())   
print(c.make_sound())  
