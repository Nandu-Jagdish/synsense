from frame import Frame
from shapes import Point, Rectangle
import cv2
import time

def main():
    main_frame = Frame(800, 600)
    rectangle = Rectangle(Point(400, 300), 100, 200, main_frame, 0)  # Initial rotation 0 degrees
    rectangle.set_colour((0, 255, 0))
    delta_degrees = 0
    while True:
        delta_degrees =delta_degrees + 30
        main_frame.show()
        # time.sleep(0.1)  # Refresh every 0.1 seconds
        rectangle.update(Point(400, 300), 100, 200, delta_degrees)  # Rotate 30 degrees on every refresh
        #exit loop after 360 degrees
        if delta_degrees == 360:
            break
if __name__ == "__main__":
    main()