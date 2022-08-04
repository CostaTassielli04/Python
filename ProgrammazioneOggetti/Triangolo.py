import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x1 = x
        self.__y1 = y

    def getx(self):
        return self.__x1

    def gety(self):
        return self.__y1

    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x1 - x), abs(self.__y1 - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle():
    def __init__(self, vertice1, vertice2, vertice3):
        self.__lista=[vertice1,vertice2,vertice3]

    def perimeter(self):
       perimetro=0
       for i in range(3):
            perimetro=perimetro+self.__lista[i].distance_from_point(self.__lista[(i+1)%3])
       return perimetro


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
