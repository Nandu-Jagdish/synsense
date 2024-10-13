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
    def __init__(self, width, height,window_name="Frame"):
        self.width = width
        self.height = height
        self.window_name = window_name
        self.frame = np.zeros((height, width, 3), np.uint8)
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # def draw_point(self, point, color=(255, 255, 255)):
    #     cv2.circle(self.frame, point, 1, color, -1)

    # def draw_line(self, point1, point2, color=(255, 255, 255)):
    #     cv2.line(self.frame, point1, point2, color, 1)

    # def draw_rectangle(self, point1, point2, color=(255, 255, 255)):
    #     cv2.rectangle(self.frame, point1, point2, color, 1)

    def __call__(self, *args, **kwds):
        return self.frame

    def show(self):
        cv2.imshow(self.window_name, self.frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class Point():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def draw_point(self, frame, radius=1, colour=(255,255,255)):
        Circle(self, radius, colour).draw(frame)

class Shape():
    def __init__(self, points, colour=(255, 255, 255)):
        self.center = points
        self.colour = colour

    def set_colour(self, colour):
        self.colour = colour

    def move(self, dx, dy):
        self.center.x += dx
        self.center.y += dy

    def get_points(self):
        raise NotImplementedError("This method cannot be called from the base class")

    def contains(self, point):
        points = self.get_points()
        points = np.array(points)
        mask = cv2.pointPolygonTest(points, (point.x, point.y), False)
        return mask >= 0


    def overlaps(self, other_shape):
        points1 = self.get_points()
        points2 = other_shape.get_points()
        points1 = np.array(points1, dtype=np.float32)
        points2 = np.array(points2, dtype=np.float32)
        intersection, _ = cv2.intersectConvexConvex(points1, points2)
        return intersection > 0

class Circle(Shape):
    def __init__(self, center, radius, colour=(255, 255, 255)):
        super().__init__(center, colour)
        self.radius = radius

    def get_points(self):
        return cv2.circle(self.center, self.radius)

    def update(self, new_center, new_radius):
        self.center = new_center
        self.radius = new_radius

    def get_points(self):
        # Approximate the circle with a polygon for intersection tests
        num_points = 100
        angles = np.linspace(0, 2 * np.pi, num_points)
        points = np.array([(self.center.x + self.radius * np.cos(angle), self.center.y + self.radius * np.sin(angle)) for angle in angles])
        return points

    def overlaps(self, other_shape):
        if isinstance(other_shape, Circle):
            # Circle-circle intersection
            distance = np.sqrt((self.center.x - other_shape.center.x) ** 2 + (self.center.y - other_shape.center.y) ** 2)
            return distance < (self.radius + other_shape.radius)
        elif isinstance(other_shape, Rectangle):
            # Circle-rectangle intersection
            rect_points = other_shape.get_points()
            for point in rect_points:
                if np.sqrt((self.center.x - point[0]) ** 2 + (self.center.y - point[1]) ** 2) < self.radius:
                    return True
            return other_shape.contains(self.center)
        else:
            # General case using polygon approximation
            return super().overlaps(other_shape)

    def draw(self, frame):
        cv2.circle(frame, (self.center.x, self.center.y), self.radius, self.colour, -1)

class Rectangle(Shape):
    def __init__(self, center,height, width,rotation_degrees=0):
        super().__init__(center)
        self.height = height
        self.width = width
        self.rotation_degrees = rotation_degrees

    def get_points(self):
        rect = ((self.center.x, self.center.y), (self.width, self.height), self.rotation_degrees)
        box = cv2.boxPoints(rect)
        box = np.int32(box)
        return box

    
    def update(self, new_center, new_height, new_width, new_rotation_degrees=0):
        self.center = new_center
        self.height = new_height
        self.width = new_width
        self.rotation_degrees = new_rotation_degrees



    # def overlaps(self, Shape):
    #     pass

    def draw(self, frame):
        rect = ((self.center.x, self.center.y), (self.width, self.height), self.rotation_degrees)
        box = cv2.boxPoints(rect)
        box = np.int32(box)
        cv2.fillPoly(frame, [box], self.colour)

class Triangle(Shape):
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3 
        centroid = self.calculate_centroid()
        super().__init__(centroid)

    def calculate_centroid(self): #TODO
        centroid_x = (self.point1.x + self.point2.x + self.point3.x) / 3
        centroid_y = (self.point1.y + self.point2.y + self.point3.y) / 3
        return Point(centroid_x, centroid_y)

    def get_points(self):
        return np.array([[self.point1.x, self.point1.y], [self.point2.x, self.point2.y], [self.point3.x, self.point3.y]]) #TODO

    def draw(self, frame):
        points = self.get_points()
        cv2.fillPoly(frame, [points], self.colour)
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
