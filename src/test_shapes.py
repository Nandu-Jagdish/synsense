import unittest
import numpy as np
import cv2

from frame import Frame
from shapes import Point, Shape, Circle, Rectangle, Triangle

class TestShapes(unittest.TestCase):

    def setUp(self):
        self.frame = Frame(800, 600)
        self.rectangle = Rectangle(Point(400, 300), 100, 200, self.frame)
        self.circle = Circle(Point(400, 300), self.frame, 50)
        self.triangle = Triangle(Point(200, 200), Point(250, 250), Point(300, 200), self.frame)
    
    def test_draw_shapes(self):
        self.rectangle.set_colour((0, 255, 0))
        # self.rectangle.draw(self.frame())
        self.circle.set_colour((0, 0, 255))
        # self.circle.draw(self.frame())
        self.triangle.set_colour((255, 0, 0))
        # self.triangle.draw(self.frame())
        self.triangle.center.draw_point(self.frame)
        self.frame.show()

    def test_rectangle_contains_point(self):
        point_inside = Point(400, 300)
        point_outside = Point(10, 20)
        self.assertTrue(self.rectangle.contains(point_inside))
        self.assertFalse(self.rectangle.contains(point_outside))

    def test_rectangle_overlaps_circle(self):
        self.assertTrue(self.rectangle.overlaps(self.circle))
        self.circle.update(Point(100, 100), 50)
        self.frame.show()
        self.assertFalse(self.rectangle.overlaps(self.circle))

    def test_rectangle_overlaps_triangle(self):
        self.assertFalse(self.rectangle.overlaps(self.triangle))
        # self.triangle.update(Point(400, 300), Point(500, 400), Point(400, 300))
        self.triangle.update(Point(350, 250), Point(250, 350), Point(350, 350))
        self.frame.show()
        self.assertTrue(self.rectangle.overlaps(self.triangle))

    def test_triangle_centroid(self):
        centroid = self.triangle.calculate_centroid()
        expected_centroid = Point(250, 216.67)  # Approximate expected centroid
        self.assertAlmostEqual(centroid.x, expected_centroid.x, places=2)
        self.assertAlmostEqual(centroid.y, expected_centroid.y, places=2)

    def test_circle_contains_point(self):
        point_inside = Point(400, 300)
        point_outside = Point(500, 500)
        self.assertTrue(self.circle.contains(point_inside))
        self.assertFalse(self.circle.contains(point_outside))

    def test_circle_overlaps_rectangle(self):
        self.assertTrue(self.circle.overlaps(self.rectangle))
        self.rectangle.update(Point(100, 100), 50, 100)
        self.assertFalse(self.circle.overlaps(self.rectangle))



    def test_remove_rectangle(self):
        self.rectangle.remove_from_frame()
        self.assertNotIn(self.rectangle, self.frame.list_of_shapes)
    
    def test_remove_circle(self):
        self.circle.remove_from_frame()
        self.assertNotIn(self.circle, self.frame.list_of_shapes)
    
    def test_remove_triangle(self):
        self.triangle.remove_from_frame()
        self.assertNotIn(self.triangle, self.frame.list_of_shapes)

if __name__ == "__main__":
    unittest.main()





# import unittest
# import numpy as np
# import cv2
# from frame import Frame
# from shapes import Point, Rectangle, Circle, Triangle

# class TestShapes(unittest.TestCase):

#     def setUp(self):
#         self.frame = Frame(800, 600)
#         self.rectangle = Rectangle(Point(400, 300), 100, 200)
#         self.circle = Circle(Point(400, 300), 50)
#         self.triangle = Triangle(Point(200, 200), Point(250, 250), Point(300, 200))

#     def test_rectangle_contains_point(self):
#         point_inside = Point(400, 300)
#         point_outside = Point(10, 20)
#         self.assertTrue(self.rectangle.contains(point_inside))
#         self.assertFalse(self.rectangle.contains(point_outside))

#     def test_rectangle_overlaps_circle(self):
#         self.assertTrue(self.rectangle.overlaps(self.circle))
#         self.circle.update(Point(100, 100), 50)
#         self.assertFalse(self.rectangle.overlaps(self.circle))

#     def test_rectangle_overlaps_triangle(self):
#         self.assertTrue(self.rectangle.overlaps(self.triangle))
#         self.triangle.update(Point(100, 100), Point(150, 150), Point(200, 100))
#         self.assertFalse(self.rectangle.overlaps(self.triangle))

#     def test_triangle_centroid(self):
#         centroid = self.triangle.calculate_centroid()
#         expected_centroid = Point(250, 216.67)  # Approximate expected centroid
#         self.assertAlmostEqual(centroid.x, expected_centroid.x, places=2)
#         self.assertAlmostEqual(centroid.y, expected_centroid.y, places=2)

#     def test_circle_contains_point(self):
#         point_inside = Point(400, 300)
#         point_outside = Point(500, 500)
#         self.assertTrue(self.circle.contains(point_inside))
#         self.assertFalse(self.circle.contains(point_outside))

#     def test_circle_overlaps_rectangle(self):
#         self.assertTrue(self.circle.overlaps(self.rectangle))
#         self.rectangle.update(Point(100, 100), 50, 100)
#         self.assertFalse(self.circle.overlaps(self.rectangle))

#     def test_draw_shapes(self):
#         self.rectangle.set_colour((0, 255, 0))
#         self.rectangle.draw(self.frame())
#         self.circle.set_colour((0, 0, 255))
#         self.circle.draw(self.frame())
#         self.triangle.set_colour((255, 0, 0))
#         self.triangle.draw(self.frame())
#         self.triangle.center.draw_point(self.frame())
#         self.frame.show()

# if __name__ == "__main__":
#     unittest.main()