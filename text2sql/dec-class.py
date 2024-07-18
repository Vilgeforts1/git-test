""" ДЕКОРАТОР ДЛЯ КЛАССА """

from math import sqrt
    
    
    
def ml_by_scalar(scalar):
    
    def class_decorator(class_to_decorate):
        
        class DecorateClass(class_to_decorate):
            
            def __init__(self, x, y, z):
                super().__init__(x, y, z)
                self.scalar = scalar
            
            def multiply(self):
                return (self.x * self.scalar,
                        self.y * self.scalar,
                        self.z * self.scalar)
                
        return DecorateClass
    return class_decorator


@ml_by_scalar(10)   
class Point:
    
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        
    def norm(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)            
                

obj = Point(1, 2, 3)

print(obj.norm())
print(obj.multiply())