class Circle():
    def __init__(self, r):
        self.r = r
        self.area=(r**2)*3.14
        self.perimeter=2*r*3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.r, self.area, self.perimeter)

class Rectangle():
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.area = h*w
        self.perimeter= 2*h+2*w

    def __str__(self):
        return "Rectangle has a hight of %.2f, a width of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.h, self.w, self.area, self.perimeter)

circle1=Circle(5)
print circle1
rectangle1=Rectangle(3,4)
print rectangle1
