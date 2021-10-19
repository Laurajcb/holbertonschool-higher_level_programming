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
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for private attribute"""
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

    def update(self, *args, **kwargs):
        """Adding the public method that assigns
        an argument to each attribute:
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if args is not None:
            properties = ['id', 'size', 'x', 'y']
            for index, arg in enumerate(args):
                if index > 3:
                    break
                setattr(self, properties[index], arg)
            return

    def to_dictionary(self):
        """Create a dict"""
        return {"id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
