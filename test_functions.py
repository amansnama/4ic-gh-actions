# Tests for functions in example_functions.py

import pytest
from example_functions import my_adder, my_thermo_stat, have_digits

# Test for my_adder
@pytest.mark.parametrize("a, b, c,sums", [(1,2,3,6),
                                          (0,-1,-4,-5),
                                          (1,100,1000.1,1101.1)])
def test_adder(a,b,c,sums):
    output=my_adder(a,b,c)
    assert output == sums

# Test for my_thermo_stat
@pytest.mark.parametrize("temp, desired_temp, status", [(70,73,'off'),
                                                        (55, 70.2, 'Heat'),
                                                        (85.2, 72, 'AC')])
def test_thermostat(temp, desired_temp, status):
    output = my_thermo_stat(temp,desired_temp)
    assert output == status

# Test for have_digits()
@pytest.mark.parametrize("s, out", [('abc123',1),
                                    ('abcd',0),
                                    ('123',1)])
def test_have_digits(s, out):
    output = have_digits(s)
    assert output == out