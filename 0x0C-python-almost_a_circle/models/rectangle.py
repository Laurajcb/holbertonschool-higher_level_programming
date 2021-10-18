#!/usr/bin/python3
"""
Rectangle class that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Raise error TypeError or ValueError"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Raise error TypeError or ValueError"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("heigth must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """Raise error"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """Raise error"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area calculation"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle
        instance with the character # """
        hash = ""
        for y in range(self.y):
            print()
        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Adding the public method that assigns
        an argument to each attribute:
        """
        if args is not None:
            properties = ['id', 'width', 'height', 'x', 'y']
            for index, arg in enumerate(args):
                setattr(self, properties[index], arg)

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Create a dict"""
        return {
                "y": self.y,
                "x": self.x,
                "id": self.id,
                "width": self.width,
                "height": self.height,
                }