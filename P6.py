#Write a program to overload subtraction for two 3D points

class point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, p):
        x = self.x - p.x
        y = self.y - p.y
        z = self.z - p.z
        return point(x, y, z)

# test:
p1 = point(5, 7, 6)
p2 = point(3, 4, 7)
p3 = p1 - p2
print(p3.x, p3.y, p3.z)
