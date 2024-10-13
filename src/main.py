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
    rectangle = Rectangle(Point(400, 300), 100, 200)
    rectangle.set_colour((0, 255, 0))
    rectangle.draw(main_frame())
    main_frame.show()
    #update rectangle
    # rectangle.update(Point(200, 200), 50, 100, 45)
    #check if point is in rectangle
    point = Point(10, 20)
    print(rectangle.contains(point))
    rectangle.draw(main_frame())

    #draw circle
    circle = Circle(Point(400, 300), 50)
    circle.set_colour((0, 0, 255))
    circle.draw(main_frame())
    #check if circle intersects with rectangle
    print(rectangle.overlaps(circle))
    main_frame.show()

    #draw triangle
    triangle = Triangle(Point(200, 200), Point(250, 250), Point(300, 200))
    triangle.set_colour((255, 0, 0))
    triangle.draw(main_frame())
    #draw the center of the triangle
    triangle.center.draw_point(main_frame())
    #check if triangle intersects with rectangle
    print(rectangle.overlaps(triangle))
    main_frame.show()


    #update rectangle


if __name__ == "__main__":

    print("Hello World")
    main()
