from math import *


def triangleSideLength(side1, side2, angle):
    '''
    computes the length of a side of a triangle given the other two sides and the angle between them
    using the cosine theorem
    :param side1: the length of one of the known sides
    :param side2: the length of the other known side
    :param angle: the angle between the 2 sides
    :return: the length of the unknown side
    '''
    c = cos(angle)
    return sqrt(side1 * side1 + side2 * side2 - 2 * side1 * side2 * cos(angle))
