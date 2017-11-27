class Circle():
    def __init__(self, r):
        self.r = r
        self.area = (r ** 2) * 3.14
        self.perimeter = 2 * r * 3.14

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.r, self.area, self.perimeter)

class Rectangle():
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

    def perimeter(self):
        return 2 * self.h + 2 * self.w

    def __str__(self):
        return "Rectangle has a hight of %.2f, a width of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.h, self.w, self.area(), self.perimeter())

class Square(Rectangle):
    def __init__(self,s):
        self.h = s
        self.w = s

    def __str__(self):
        return "Square has a side length of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.h, self.area(), self.perimeter())

class RightTriangle():
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return 0.5 * self.h * self.w

    def hypotenuse(self):
        return 0.5 ** (self.h ** 2 + self.w ** 2)

    def perimeter(self):
        return self.hypotenuse() + self.h + self.w

    def __str__(self):
        return "Square has a hight of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.h, self.area(), self.perimeter())
##finish __str__ 
class EqualateralRightTriangle(RightTriangle):
    def __init__(self, s):
        self.h = s
        self.w = s


circle1=Circle(5)
print circle1
rectangle1=Rectangle(3,4)
print rectangle1
square1=Square(6)
print square1
