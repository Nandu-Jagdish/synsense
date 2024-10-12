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

class Frame():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frame = np.zeros((height, width, 3), np.uint8)

    # def draw_point(self, point, color=(255, 255, 255)):
    #     cv2.circle(self.frame, point, 1, color, -1)

    # def draw_line(self, point1, point2, color=(255, 255, 255)):
    #     cv2.line(self.frame, point1, point2, color, 1)

    # def draw_rectangle(self, point1, point2, color=(255, 255, 255)):
    #     cv2.rectangle(self.frame, point1, point2, color, 1)

    def __call__(self, *args, **kwds):
        return self.frame

    def show(self):
        cv2.imshow("Frame", self.frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class shape():
    def __init__(self, points):
        self.center = points
        self.colour = (255, 255, 255)

    def set_colour(self, colour):
        self.colour = colour


    def contains(self, point):
        pass

    def overlaps(self, shape):
        pass

class Rectangle(shape):
    def __init__(self, center,height, width):
        super().__init__(center)
        self.height = height
        self.width = width
    

    
    def move(self, dx, dy):
        self.center.x += dx
        self.center.y += dy
    
    def update(self, new_center, new_height, new_width):
        self.center = new_center
        self.height = new_height
        self.width = new_width

    def contains(self, point):
        pass

    def overlaps(self, shape):
        pass

    def draw(self, frame):
        cv2.rectangle(frame, (self.center.x - self.width//2, self.center.y - self.height//2), (self.center.x + self.width//2, self.center.y + self.height//2), self.colour, -1)

def main():
    main_frame = Frame(800, 600)
    rectangle = Rectangle(Point(400, 300), 100, 200)
    rectangle.set_colour((0, 255, 0))
    rectangle.draw(main_frame())
    main_frame.show()
    #update rectangle
    # rectangle.update(Point(200, 200), 50, 100)
    # rectangle.draw(main_frame())
    main_frame.show()

    #update rectangle


if __name__ == "__main__":

    print("Hello World")
    main()
