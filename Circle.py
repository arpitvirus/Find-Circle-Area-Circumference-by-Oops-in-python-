import math
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius

p1 = circle(5)
print(p1.area()) 
print(p1.perimeter())

