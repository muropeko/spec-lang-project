class Bresenham:
    @staticmethod
    def draw(x1, y1, x2, y2):
        points = []
        dx = x2 - x1
        dy = y2 - y1
        sx = 1 if dx > 0 else -1
        sy = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            err = dx / 2.0
            while x1 != x2:
                points.append((x1, y1))
                err -= dy
                if err < 0:
                    y1 += sy
                    err += dx
                x1 += sx
            points.append((x2, y2))
        else:
            err = dy / 2.0
            while y1 != y2:
                points.append((x1, y1))
                err -= dx
                if err < 0:
                    x1 += sx
                    err += dy
                y1 += sy
            points.append((x2, y2))

        return points
