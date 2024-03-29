#!/usr/bin/python3

class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """validate a parameter as a value

    Args:
        name (str): The name of the parameter
        value (int): the parameter to validate

    Raises:
        TypeError: If value is not an integer 
        ValueError: If value is <= 0
        """
    if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


