
class Point:
    def __init__(self, x_init: float, y_init: float):
        self.__x = x_init
        self.__y = y_init

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return (self.x == other.x) & (self.y == other.y)
        return False

    def __hash__(self):
        return hash(str(self))


def distance(p1: Point, p2: Point):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5


class Circle:
    def __init__(self, x: float, y: float, r: float):
        self.__center = Point(x, y)
        self.__radius = r

    @property
    def center(self) -> Point:
        return self.__center

    @property
    def radius(self) -> float:
        return self.__radius

    @center.setter
    def center(self, c):
        self.__center = c

    @radius.setter
    def radius(self, r):
        self.__radius = r

    def __repr__(self):
        return "".join(["Circle(", str(self.center.x), ", ", str(self.center.y), ", ", str(self.radius), ")"])

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Circle):
            return (self.center.x == other.center.x) & (self.center.y == other.center.y) & (self.radius == other.radius)
        return False


class Trilateration:
    """
    holds a list of beacons and a result of the trilateration
    after solve_history was called on the Trilateration object
    """
    def __init__(self, beacons: [Circle], result: Circle = None):
        self.__beacons = beacons
        self.__result = result

    @property
    def beacons(self):
        return self.__beacons

    @property
    def result(self):
        return self.__result

    @beacons.setter
    def beacons(self, b):
        self.__beacons = b

    @result.setter
    def result(self, r):
        self.__result = r
