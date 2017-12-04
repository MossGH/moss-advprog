class Circle():
    def __init__(self, r):
        self.r = r

    def area(self):
        return (self.r ** 2) * 3.14

    def perimeter(self):
        return self.r * 6.28

    def __str__(self):
        return "Circle has a radius of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.r, self.area, self.perimeter)

class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def __str__(self):
        return "Rectangle has a hight of %.2f, a width of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.y, self.x, self.area(), self.perimeter())

class Square(Rectangle):
    def __init__(self,x):
        self.x = x
        self.y = x

    def __str__(self):
        return "Square has a side length of %.2f, an area of %.2f, and a perimeter of %.2f." % (self.y, self.area(), self.perimeter())

class RightTriangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hyp = self.hypotenuse()

    def area(self):
        return 0.5 * self.x * self.y

    def hypotenuse(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def perimeter(self):
        return self.hyp + self.x + self.y

    def __str__(self):
        return "Triangle has a hight of %.2f, a base of %.2f an area of %.2f, and a perimeter of %.2f." % (self.y, self.x, self.area(), self.perimeter())

class EquilateralRightTriangle(RightTriangle):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.hyp = self.hypotenuse()

    def __str__(self):
        return "Triangle has a base and hight of %.2f an area of %.2f, and a perimeter of %.2f." % (self.y, self.area(), self.perimeter())

class Prism():
    def surfacearea(self):
        return 2 * self.area() + self.z * self.perimeter()

    def volume(self):
        return self.area() * self.z

class Cube(Square,Prism):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.z = x

    def __str__(self):
        return "Cube has a width, hieght, and depth of %.2f, a surfacearea of %.2f, and a volume of %.2f." % (self.x, self.surfacearea(), self.volume())

class TriangularPrism(RightTriangle,Prism):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.hyp = self.hypotenuse()

    def __str__(self):
        return "Triangular Prism has a width of %.2f, a hieght of %.2f, a depth of %.2f, a surfacearea of %.2f, and a volume of %.2f." % (self.x, self.y, self.z, self.surfacearea(), self.volume())

class Cylinder(Circle,Prism):
    def __init__(self, r, z):
        self.r = r
        self.z = z

    def __str__(self):
        return "Cylinder has a radius of %.2f, a hieght of %.2f, a surfacearea of %.2f, and a volume of %.2f." % (self.r, self.z, self.surfacearea(), self.volume())

# circle1=Circle(5)
# print circle1
# rectangle1=Rectangle(3,4)
# print rectangle1s
# square1=Square(6)
# print square1
# RT=RightTriangle(3,4)
# print RT
# ERT=EquilateralRightTriangle(2)
# print ERT
# Cube1=Cube(4)
# print Cube1
# TP=TriangularPrism(3,5)
# print TP
Cyl=Cylinder(1,2)
print Cyl
