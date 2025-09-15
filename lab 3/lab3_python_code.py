
# create classes
class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def getArea(self):
        return self.l * self.w
    
class Circle(Shape):
    def __init__(self, r):
        self.radius = r
        
    def getArea(self):
        return 3.14 * self.radius * self.radius  
    
class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    
    def getArea(self):
        return 0.5 * self.height * self.base  

# read txt file
with open(r'C:\Users\Jordan\Desktop\shape.txt', 'r') as file:  
    lines = file.readlines()


for line in lines:
    components = line.strip().split(',')  
    shape = components[0].strip()

    if shape == 'Rectangle':
        rect = Rectangle(int(components[1]), int(components[2]))
        print('Area of rectangle is:', rect.getArea())
    elif shape == 'Circle':   
        cirl = Circle(int(components[1]))
        print('Area of circle is:', cirl.getArea())
    elif shape == 'Triangle':
        tri = Triangle(int(components[1]), int(components[2]))
        print('Area of triangle is:', tri.getArea())
    else:
        pass