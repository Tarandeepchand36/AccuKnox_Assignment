class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Implementing the __iter__ method to allow iteration over the instance
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(7, 3)

# Iterating over the instance to print the length and width
for dimension in rect:
    print(dimension)