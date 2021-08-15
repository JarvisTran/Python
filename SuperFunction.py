class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    def Area(self):
        return self.length*self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.height = height
        super().__init__(length, width)
    def Volume(self):
        return self.height*self.width*self.length


square = Square(3,3)
cube = Cube(3,3,3)

print(square.Area())
print(cube.Volume())