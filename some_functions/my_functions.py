"""Functions to calculate area and perimeter of a rectangle.

Functions for examples_tests.py, renamed to test_example.py

- `area_of_rectangle(width, height)` - Returns area.
- `perimeter_of_rectangle(width, height)` - Returns perimeter.

Examples:
    >>> from some_functions import my_functions
    >>> my_functions.area_of_rectangle(10,2)
    20
    >>> my_functions.perimeter_of_rectangle(1.1, 5)
    12.2
"""

def area_of_rectangle(width: int | float, height: int | float) -> int | float:
    """Calculates area of rectangle.

    Args:
        width (int | float): width of rectangle
        height (int | float): height of rectangle

    Returns:
        area = width times height
    """
    return width*height


def perimeter_of_rectangle(width: int | float, height: int | float) -> int | float:
    """Calculates perimeter of a rectangle

    Args:
        width (int | float): width of rectangle
        height (int | float): height of rectangle

    Returns:
        perimeter = 2 * (width + height)
    """
    return 2*(width+height)
