class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)

r1 = Rectangle(10, 5)
print(f'Area is {r1.area()}')
print(f'Perimeter is {r1.perimeter()}')

r2 = Rectangle(15, 10)
print(f'Area is {r2.area()}')
print(f'Perimeter is {r2.perimeter()}')