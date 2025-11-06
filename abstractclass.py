from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass
class Dog(Animal):
    def makesound(self):
        return "Woof!"
class Cat(Animal):
    def makesound(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.makesound())  
print(cat.makesound())  
