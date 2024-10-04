# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

def my_adder(a: int | float, b: int | float, c: int | float) -> int | float:
    """Sums three numbers.

    function to sum the 3 numbers
    Input: 3 numbers a, b, c
    Output: the sum of a, b, and c
    author: Aman S
    Date: Sep 20 2024
    """

    # this is the summation
    out = a + b + c

    return out


def my_thermo_stat(temp: int | float, desired_temp: int | float) -> str:
    """Change thermostat.

    Changes the status of the thermostat based on 
    temperature and desired temperature
    author: Aman S
    Date: Sep 20 2024
    :type temp: Int
    :type desiredTemp: Int
    :rtype: String
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status


def have_digits(s: str) -> int:
    """Check digits

    Checks if a string has digits in it
    Author: Aman S
    Date: Sep 20 2024
    """

    out = 0

    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break

    return out
