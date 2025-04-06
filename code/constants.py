
#!/usr/bin/env python
"""
--------------------------------
project: code
created: 11/04/2018 18:02
---------------------------------

"""
import os

"""These lines calculate the absolute path to a directory named 'data' 
that is located in the parent directory of the current script. This is
 a common way to define the location of project data relative to the code."""
class Paths(object):
    data = os.path.abspath(
            os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    os.pardir,
                    'data'
            )
    )

    output = os.path.join(data, 'exercise_output')
    input = os.path.join(data, 'exercise_input')

paths = Paths()