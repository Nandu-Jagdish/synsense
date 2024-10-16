"""

Main script for programing task:

Design and code a set of classes in Python for defining and manipulating
two-dimensional geometric shapes. A user should be able to define points
and at least two shapes (e.g. rectangle; triangle; circle). User should be
able to determine whether an arbitrary point is contained within a shape,
and whether two shapes overlap. The classes should have a clean inheri-
tance hierarchy, and be well-documented. Methods do not need to be fully
implemented, but can exist as stubs.

Opencv is heavily used in this project. Please install using requirements.txt


Author: Nandu Jagdish
email: nandu.workmail@gmail.com


"""

import cv2
import numpy as np


from frame import Frame
from shapes import Point, Shape, Circle, Rectangle, Triangle


def main():
    main_frame = Frame(800, 600)
    rectangle = Rectangle(Point(400, 300), 100, 200,main_frame)
    rectangle.set_colour((0, 255, 0))


    #update rectangle
    rectangle.update(Point(200, 200), 50, 100, 45)
    #check if point is in rectangle
    point = Point(10, 20)
    if rectangle.contains(point):
        print("Point is in rectangle")
    else:
        print("Point is not in rectangle")
    main_frame.show()

    #draw circle
    circle = Circle(Point(400, 300),main_frame, 50)
    circle.set_colour((0, 0, 255))

    #check if circle intersects with rectangle
    if circle.overlaps(rectangle):
        print("Circle overlaps with rectangle")
    else:
        print("Circle does not overlap with rectangle")

    main_frame.show()

    #draw triangle
    triangle = Triangle(Point(200, 200), Point(250, 250), Point(300, 200),main_frame)
    triangle.set_colour((255, 0, 0))
    main_frame.show()
    #draw the center of the triangle
    triangle.center.draw_point(main_frame)
    #check if triangle intersects with rectangle
    rectangle.update(Point(50, 200), 50, 100, 45)
    main_frame.show()
    if rectangle.overlaps(triangle):
        print("Triangle overlaps with rectangle")
    else:
        print("Triangle does not overlap with rectangle")

        # remove rectangle
    rectangle.remove_from_frame()
    print("Rectangle deleted")
    main_frame.show()

    #check if point is in circle
    point = Point(400, 300)
    if circle.contains(point):
        print("Point is in circle")
    else:
        print("Point is not in circle")


    main_frame.show()


    #update rectangle


if __name__ == "__main__":

    print("Hello World")
    main()
