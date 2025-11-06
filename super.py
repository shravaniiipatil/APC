class Animal:
    def sound(self):
        print("Animals make sound")
class Dog(Animal):
    def sound(self):
        super().sound()   
        print("Dog barks")
d = Dog()
d.sound()
