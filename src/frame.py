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

    Methods
    -------
    __call__(*args, **kwds):
        Returns the frame image data.
    show():
        Displays the frame in a window.
    __del__():
        Cleans up the window when the object is destroyed.
    """
    def __init__(self, width, height,window_name="Frame"):
        self.width = width
        self.height = height
        self.window_name = window_name
        self.frame = np.zeros((height, width, 3), np.uint8)
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
        Displays the frame in a window.
        """
        cv2.imshow(self.window_name, self.frame)
        cv2.waitKey(0)
        # cv2.destroyAllWindows()
    def __del__(self):
        """
        Cleans up the window when the object is destroyed.
        """
        # cv2.destroyAllWindows()
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