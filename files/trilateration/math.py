
from scipy.optimize import least_squares
from trilateration.geometry import Trilateration, Circle, Point
import math


def solve_history(history: [Trilateration], guess=Circle(0, 0, 0)):
    """solves a list of Trilateration objects. Remembers last guess"""
    for item in history:
        guess = solve(item, guess)


def solve(trilateration, guess: Circle = Circle(0, 0, 0)) -> Circle:
    """stores a trilateration result and returns it"""
    result = easy_least_squares(trilateration.beacons, guess)
    trilateration.result = result
    return result


def get_intersect(circle_1: Circle, circle_2: Circle) -> Point:
    """Returns the positive intersection point of two circles"""
    d = circle_2.center.x - circle_1.center.x
    x = (circle_1.radius**2 - circle_2.radius**2 + d**2)/(2*d)
    y = (circle_1.radius**2 - x**2)**0.5
    return Point(x, y)


def easy_least_squares(beacons: list, guess=Circle(0, 0, 0)) -> Circle:
    """Finds a trilateration result for multiple beacons"""
    g = (guess.center.x, guess.center.y, guess.radius)
    result = least_squares(equations, g, args=[beacons])
    xf, yf, rf = result.x
    return Circle(xf, yf, rf)


def equations(guess, crls: [Circle]):
    """equations to find an optimized solution for"""
    eqs = []
    x, y, r = guess
    for circle in crls:
        eqs.append(((x - circle.center.x) ** 2 + (y - circle.center.y) ** 2 - (circle.radius - r) ** 2))
    return eqs

def accuracy(data, target_pos):
    '''data: list of lists of tuples (for multiple measurements)
    target_pos: exact (x,y) tuple of target
    accuracy gives the mean distance from measured points to the target'''
    length = 0
    x1,y1 = target_pos[0], target_pos[1]
    means = []
    for dataset in data:
        dis = [math.hypot(x-x1, y-y1) for x,y in dataset]
        length += len(dataset)
        means += dis
    return means.sum() / length 

def gain(accuracies):
    gains = [(accuracies[i]-accuracies[i-1])/accuracies[i-1] for i in range(1, len(accuracies)-1)]
    return gains

