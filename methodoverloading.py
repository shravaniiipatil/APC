class MathOperation:
    def add(self, a=0, b=0, c=0):
        return a + b + c
obj = MathOperation()
print(obj.add(5, 10))      
print(obj.add(5, 10, 20)) 
print(obj.add(5))          


class MathOperation:
    def add(self, *args):
        return sum(args)
obj = MathOperation()
print(obj.add(2, 3))            
print(obj.add(1, 2, 3, 4, 5))  
