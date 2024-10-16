import cv2
import numpy as np
from frame import Frame

class Point():
    """
    A class to represent a point in 2D space.
    NOTE: I would personally use the numpy array for this but for the sake OO design, I am using this class. Using numpy arrays would be more efficient.
    
    Attributes
    ----------
    x : int
        The x-coordinate of the point.
    y : int
        The y-coordinate of the point.

    Methods
    -------
    __str__():
        Returns a string representation of the point.
    draw_point(frame, radius=1, colour=(255,255,255)):
        Draws the point on a frame.


    """
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def draw_point(self, frame, radius=1, colour=(255,255,255)):
        """
        Draws the point on a frame. Default radius is 1 and colour is white. Can be usefull when debuging.
        """
        Circle(self,frame, radius, colour)

class Shape():
    """
    Base class for all shapes. Contains methods for moving shapes, changing colours, and checking if a point is contained within the shape.
    
    Attributes
    ----------
    center : Point
        The center of the shape.
    colour : tuple
        The colour of the shape. In BGR format.(opencv uses BGR format)
    frame : Frame
        The frame to draw the shape on.
    Methods
    -------
    set_colour(colour):
        Sets the colour of the shape.
    move(dx, dy):
        Moves the shape by dx and dy.
    get_points():
        Returns the points of the shape. This method should be overridden by subclasses.
    contains(point):
        Returns True if the point is contained within the shape. This can be overridden by subclasses.
    overlaps(other_shape):
        Returns True if the shape overlaps with another shape. This can be overridden by subclasses.



    
    """
    def __init__(self, points,frame, colour=(255, 255, 255)):
        """
        Initializes the shape with a center and colour."""

        self.center = points
        self.colour = colour
        self.frame = frame
        self.add_to_frame()

    # def __del__(self):
    #     """
    #     Removes the shape from the frame when the object is destroyed.
    #     """
    #     # print(f"{self.__class__.__name__} object is being deleted")
    #     self.frame.remove_shape(self)

    def remove_from_frame(self):
        """
        Removes the shape from the frame.

        NOTE: This method exists because the __del__ method is not called when the object is deleted from a list for some wierd reason.
        """
        self.frame.remove_shape(self)
        del self


    def add_to_frame(self):
        """
        Adds the shape to the frame.
        """
        self.frame.add_shape(self)

    def set_colour(self, colour):
        """
        Sets the colour of the shape.
        
        Parameters
        ----------
        colour : tuple
            The colour of the shape in BGR format.
        """
        self.colour = colour


    def get_points(self):
        """
        Returns the points of the shape. This method should be overridden by subclasses.
        """
        raise NotImplementedError("This method cannot be called from the base class")

    def contains(self, point):
        """
        Returns True if the point is contained within the shape. This can be overridden by subclasses.

        Parameters
        ----------
        point : Point
            The point to check.
        
        Returns
        -------
        bool
            True if the point is contained within the shape.

        using the cv2.pointPolygonTest method to check if the point is inside the shape.
        """
        points = self.get_points()
        points = np.array(points)
        mask = cv2.pointPolygonTest(points, (point.x, point.y), False)
        return mask >= 0


    def overlaps(self, other_shape):
        """
        Returns True if the shape overlaps with another shape. This can be overridden by subclasses.

        Parameters
        ----------
        other_shape : Shape
            The other shape to check for overlap.

        Returns
        -------
        bool
            True if the shape overlaps with the other shape.

        """
        points1 = self.get_points()
        points2 = other_shape.get_points()
        points1 = np.array(points1, dtype=np.float32)
        points2 = np.array(points2, dtype=np.float32)
        intersection, _ = cv2.intersectConvexConvex(points1, points2)
        return intersection > 0

class Circle(Shape):
    """
    A class to represent a circle.
    Attributes
    ----------
    center : Point
        The center of the circle.
    radius : int
        The radius of the circle.
    frame : Frame
        The frame to draw the circle on.
    colour : tuple
        The colour of the circle. In BGR format.

    Methods
    -------
    update(new_center, new_radius):
        Updates the center and radius of the circle.
    get_points():
        Returns the points of the circle.
    overlaps(other_shape):
        Returns True if the circle overlaps with another shape.
    draw(frame):
        Draws the circle on a frame.
    
    

        """
    def __init__(self, center,frame, radius, colour=(255, 255, 255)):
        """
        Initializes the circle with a center, radius, and colour.
        
        Parameters
        ----------
        center : Point
            The center of the circle.
        radius : int
            The radius of the circle.
        frame : Frame
            The frame to draw the circle on.
        colour : tuple
            The colour of the circle in BGR format.

            """
        super().__init__(center,frame, colour)
        self.radius = radius


    # def get_points(self):
    #     return cv2.circle(self.center, self.radius)

    def update(self, new_center, new_radius):
        """
        Updates the center and radius of the circle.
        
        Parameters
        ----------
        new_center : Point
            The new center of the circle.
        new_radius : int
            The new radius of the circle.
        """

        
        self.center = new_center
        self.radius = new_radius

    def get_points(self):
        """
        Returns the points of the circle.

        Returns
        -------
        np.ndarray
            The points of the circle. Approximated by a polygon.

        """
        # Approximate the circle with a polygon for intersection tests
        num_points = 100
        angles = np.linspace(0, 2 * np.pi, num_points)
        points = np.array([(self.center.x + self.radius * np.cos(angle), self.center.y + self.radius * np.sin(angle)) for angle in angles], dtype=np.int32)
        return points

    def overlaps(self, other_shape):
        """
        Returns True if the circle overlaps with another shape.

        Parameters
        ----------
        other_shape : Shape
            The other shape to check for overlap.

        Returns
        -------
        bool
            True if the circle overlaps with the other shape.

        """
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
        """
        Draws the circle on a frame.

        Parameters
        ----------
        frame : np.ndarray         
             The frame to draw the circle on.  
        """
        cv2.circle(frame, (self.center.x, self.center.y), self.radius, self.colour, -1)

class Rectangle(Shape):
    """
    A class used to represent a Rectangle, inheriting from Shape.
    Attributes
    ----------
    center : Point
        The center point of the rectangle.
    height : float
        The height of the rectangle.
    width : float
        The width of the rectangle.
    rotation_degrees : float, optional
        The rotation of the rectangle in degrees (default is 0).
    Methods
    -------
    get_points():
        Returns the four corner points of the rectangle as a numpy array of integers.
    update(new_center, new_height, new_width, new_rotation_degrees=0):
        Updates the rectangle's center, height, width, and rotation.
    draw(frame):
        Draws the rectangle on the given frame.
    """
    def __init__(self, center,height, width,frame,rotation_degrees=0):


        """
        Initializes a shape with a center, height, width, and optional rotation.

        Parameters
        ----------
        center : tuple
            The (x, y) coordinates of the shape's center.
        height : float
            The height of the shape.
        width : float
            The width of the shape.
        rotation_degrees : float, optional
            The rotation of the shape in degrees. Defaults to 0.
        """
        super().__init__(center,frame)
        self.height = height
        self.width = width
        self.rotation_degrees = rotation_degrees
    


    def get_points(self):
        """
        Calculate the four vertices of a rotated rectangle.

        This method computes the four corner points of a rectangle given its center,
        dimensions (width and height), and rotation angle in degrees. The rectangle
        is represented as a tuple containing the center coordinates, dimensions, and
        rotation angle. The method uses OpenCV's `boxPoints` function to determine
        the vertices and converts them to integer coordinates.

        Returns:
            numpy.ndarray: A 2D array of shape (4, 2) containing the integer coordinates
                           of the four vertices of the rotated rectangle.
        """
        rect = ((self.center.x, self.center.y), (self.width, self.height), self.rotation_degrees)
        box = cv2.boxPoints(rect)
        box = np.int32(box)
        return box

    
    def update(self, new_center, new_height, new_width, new_rotation_degrees=0):
        """
        Update the properties of the shape.

        Parameters:
        -----------
        new_center (tuple): A tuple representing the new center coordinates (x, y) of the shape.
        new_height (float): The new height of the shape.
        new_width (float): The new width of the shape.
        new_rotation_degrees (float, optional): The new rotation of the shape in degrees. Defaults to 0.


        """
        self.center = new_center
        self.height = new_height
        self.width = new_width
        self.rotation_degrees = new_rotation_degrees



    # def overlaps(self, Shape):
    #     pass

    def draw(self, frame):
        """
        Draw the rectangle on the given frame.

        Parameters:
        -----------
        frame (numpy.ndarray): The frame on which to draw the rectangle.   
            
            """
        rect = ((self.center.x, self.center.y), (self.width, self.height), self.rotation_degrees)
        box = cv2.boxPoints(rect)
        box = np.int32(box)
        cv2.fillPoly(frame, [box], self.colour)

class Triangle(Shape):
    """
    A class to represent a triangle.

    Attributes
    ----------
    point1 : Point
        The first point of the triangle.
    point2 : Point
        The second point of the triangle.
    point3 : Point
        The third point of the triangle.
    frame : Frame
        The frame to draw the triangle on.

    Methods
    -------
    calculate_centroid():
        Calculates the centroid of the triangle.
    get_points():
        Returns the points of the triangle.
    draw(frame):
        Draws the triangle on a frame.

    """
    def __init__(self, point1, point2, point3,frame):
        """
        Initializes the triangle with three points.

        Parameters
        ----------
        point1 : Point

        point2 : Point

        point3 : Point

        Computes the centroid of the triangle and initializes the shape with the centroid.

        """
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3 
        centroid = self.calculate_centroid()
        super().__init__(centroid,frame)

    def calculate_centroid(self):
        """
        Calculates the centroid of the triangle.

        NOTE: could be done using numpy arrays for efficiency.

        Returns
        -------
        Point 
            The centroid of the triangle.
                
            """
        centroid_x = (self.point1.x + self.point2.x + self.point3.x) / 3
        centroid_y = (self.point1.y + self.point2.y + self.point3.y) / 3
        return Point(centroid_x, centroid_y)
    
    def update(self, point1, point2, point3):
        """
        Updates the points of the triangle.

        Parameters
        ----------
        point1 : Point

        point2 : Point

        point3 : Point

        """
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def get_points(self):
        """
        Returns the points of the triangle.

        NOTE: This function could have been avoided if we used numpy arrays for the points.

        Returns
        -------
        np.ndarray
            The points of the triangle.
        """
        return np.array([[self.point1.x, self.point1.y], [self.point2.x, self.point2.y], [self.point3.x, self.point3.y]]) 

    def draw(self, frame):
        """
        Draws the triangle on a frame.

        Parameters
        ----------
        frame : np.ndarray
            The frame to draw the triangle on.
        """
        points = self.get_points()
        cv2.fillPoly(frame, [points], self.colour)

