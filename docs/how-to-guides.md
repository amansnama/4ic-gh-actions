## How to import the package 'some_functions'

If you have the entire package `some_functions` instead of the individual `.py` files, importing the package as a whole can be done.

1. Ensure `some_functions` is in the project directory.
2. Import the modules as:
`from some_functions import example_functions, my_functions`
3. Run the functions in the modules:
```
>>> example_functions.my_thermo_stat(75,69)
'AC'
>>> my_functions.perimeter_of_rectangle(1.1, 5)
12.2
```

## How to import if 'some_functions' is not in project directory

If `some_functions` is located outside the project directory, the import statement will not find the package and will raise an error. To import `some_functions` in this case, add the path to the package to the system path variable (it defines the import search path). Then import the modules. The Python code looks like:
```
import sys
sys.path.insert(0, "path/to/some_functions/")

from some_functions import example_functions, my_functions
```
Replace "path/to/some_functions/" in the above code snippet with the actual path to `some_functions`.

Relevant stackoverflow: https://stackoverflow.com/questions/24868733/how-to-access-a-module-from-outside-your-file-folder-in-python