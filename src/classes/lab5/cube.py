from src.classes.lab5.bresenham import Bresenham

class Cube:
    def __init__(self, size):
        self.x = 5
        self.y = 5
        self.z = 5
        self.size = size

    def draw(self):
        vertices = [
            (self.x, self.y, self.z),
            (self.x + self.size, self.y, self.z),
            (self.x + self.size, self.y + self.size, self.z),
            (self.x, self.y + self.size, self.z),
            (self.x, self.y, self.z + self.size),
            (self.x + self.size, self.y, self.z + self.size),
            (self.x + self.size, self.y + self.size, self.z + self.size),
            (self.x, self.y + self.size, self.z + self.size)
        ]

        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        points = []
        for edge in edges:
            start, end = vertices[edge[0]], vertices[edge[1]]
            x1, y1 = start[0] - start[2] // 2 + self.size // 2, start[1] - start[2] // 2 + self.size // 2
            x2, y2 = end[0] - end[2] // 2 + self.size // 2, end[1] - end[2] // 2 + self.size // 2
            points += Bresenham.draw(x1, y1, x2, y2)

        return points
