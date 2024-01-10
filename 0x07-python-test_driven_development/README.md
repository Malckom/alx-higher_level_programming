Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown.

Developers commonly use doctest to test documentation. The doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the command’s input given in the docstrings test example.

The default action when running doctests is not to show the output when a test passes. However, we can change this in the doctest runner options. In addition, doctest’s integration with the Python unittest module enables us to run doctests as standard unittest test cases.


