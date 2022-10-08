from trilateration.math import get_intersect, easy_least_squares
from trilateration.geometry import Trilateration, Circle, Point
import serial

C1_offset = 5			#0x1EB82
C2_offset = 3.5			#0x1F084
C3_offset = 6			#0x1EBEE

Circle_1 = Circle(0,0,12)
Circle_2 = Circle(12,0,12)
Circle_3_center = get_intersect(Circle_1, Circle_2)
print("Cienter of Circle 3", Circle_3_center)


def get_triangulation_ponint(r1 = 10, r2=5, r3=6):


    C1 = Circle(0,0,r1-C1_offset)
    C2 = Circle(0,0,r2-C2_offset)
    C3 = Circle(Circle_3_center.x, Circle_3_center.y, r3-C3_offset)
    return easy_least_squares((C1,C2,C3))

get_triangulation_ponint()