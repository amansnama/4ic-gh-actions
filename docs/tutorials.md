In this tutorial, we will import the module and learn to run the functions inside the module.

## Importing the module

1. Place the files in the same directory: Ensure that my_functions.py and example_functions.py are in the same directory as your main script or in the current working directory (if you are using Python interactively).
2. Create a new python script.
3. Import the functions at the top of the script.
```
import my_functions
import example_functions
```
We must always import the modules before using the functions within it.

## Using the function

1. To use functions in my_functions, for example area_of_rectangle():
`area = my_functions.area_of_rectangle(width=5, height=4))`
2. Print the area:
`print("The area of the rectangle is", area)`
3. The output will be:
`The area of the rectangle is 20`
4. Functions in example_functions can be called similarly.
```
>>> example_functions.my_adder(1,2,3)
6
>>> example_functions.have_digits("abc")
0
```

## Example of python script

A complete python script to import and run the functions will look like:
```
# main.py
import my_functions
import example_functions

# Sum three numbers.
print(" Sum of 1, 2, and 3 =", example_functions.my_adder(1,2,3))
```
Run the script with:
`python main.py`

The output should look like
`Sum of 1, 2, and 3 = 6`