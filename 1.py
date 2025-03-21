class Rectangle:        #определение класса
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

#определение объектов
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Прямоугольник 1: площадь = {rect1.area()}, периметр = {rect1.perimeter()}")
print(f"Прямоугольник 2: площадь = {rect2.area()}, периметр = {rect2.perimeter()}")
