class RectangleLand:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")