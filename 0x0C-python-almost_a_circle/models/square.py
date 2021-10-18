#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a Squeare class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """Defines the print"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Create a dict"""
        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }