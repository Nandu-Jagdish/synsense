"""
Module Name: frame.py
Description: This module contains the Frame class which is used to display images using OpenCV.

Author: Nandu Jagdish
"""

import cv2
import numpy as np

class Frame():
    """
    A class to represent a frame for displaying images using OpenCV.

    Attributes
    ----------
    width : int
        The width of the frame.
    height : int
        The height of the frame.
    window_name : str
        The name of the window where the frame will be displayed.
    frame : np.ndarray
        The image data for the frame.
    list_of_shapes : list
        A list of shapes to be displayed

    Methods
    -------
    __call__(*args, **kwds):
        Returns the frame image data.
    show():
        Displays the frame in a window.
    add_shape(shape):
        Adds a shape to the frame.
    draw_shapes():
        Draws all the shapes on the frame.
    remove_shape(shape):
        Removes a shape from the frame.
    refresh():
        Refreshes the frame by clearing the image data and redrawing all shapes.
    __del__():
        Cleans up the window when the object is destroyed.
    """
    def __init__(self, width, height,window_name="Frame"):
        self.width = width
        self.height = height
        self.window_name = window_name
        self.frame = np.zeros((height, width, 3), np.uint8)
        self.list_of_shapes = []
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)


    def __call__(self, *args, **kwds):
        """
        Returns the frame image data.

        Returns
        -------
        np.ndarray
            The image data for the frame.
       
        """
        return self.frame

    def show(self):
        """
        Refreshed and displays the frame in a window.
        """
        self.refresh()
        cv2.imshow(self.window_name, self.frame)
        cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def add_shape(self, shape):
        """
        Adds a shape to the frame.

        Parameters
        ----------
        shape : Shape
            The shape to add to the frame.
        """
        self.list_of_shapes.append(shape)

    def draw_shapes(self):
        """
        Draws all the shapes on the frame.
        """
        for shape in self.list_of_shapes:
            shape.draw(self.frame)
    def remove_shape(self, shape):
        """
        Removes a shape from the frame.

        Parameters
        ----------
        shape : Shape
            The shape to remove from the frame.
        """
        self.list_of_shapes.remove(shape)

    def refresh(self):
        """
        Refreshes the frame by clearing the image data and redrawing all shapes.
        """
        self.frame = np.zeros((self.height, self.width, 3), np.uint8)
        self.draw_shapes()

    def __del__(self):
        """
        Cleans up the window when the object is destroyed.
        """
        # cv2.destroyAllWindows()
        print("Destroying window")
        cv2.destroyWindow(self.window_name)


# class Frame():
#     def __init__(self, width, height,window_name="Frame"):
#         self.width = width
#         self.height = height
#         self.window_name = window_name
#         self.frame = np.zeros((height, width, 3), np.uint8)
#         cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

#     # def draw_point(self, point, color=(255, 255, 255)):
#     #     cv2.circle(self.frame, point, 1, color, -1)

#     # def draw_line(self, point1, point2, color=(255, 255, 255)):
#     #     cv2.line(self.frame, point1, point2, color, 1)

#     # def draw_rectangle(self, point1, point2, color=(255, 255, 255)):
#     #     cv2.rectangle(self.frame, point1, point2, color, 1)

#     def __call__(self, *args, **kwds):
#         return self.frame

#     def show(self):
#         cv2.imshow(self.window_name, self.frame)
#         cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#     def __del__(self):
#         cv2.destroyWindow(self.window_name)
#         pass