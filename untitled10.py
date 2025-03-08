# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:18:33 2024

@author: husse
"""
'''c = (0, 7)
match c:
    case (0, 0):
        print('this is the origin')
    case (x, 0):
        print(f"X={x}")
    case (0, y):
        print(f"Y={y}")
    case (x, y):
        print(f"X={x}, Y={y}") '''





class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

c = Point(0,5)


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=var):
            print(f"Y={var}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")