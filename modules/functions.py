"""
==========
Functions
==========
Where we keep the useful functions
----------------------------------
"""


def add_ten(param):
    """
    Function adds ten to the given input parameters:

    Args:
        param(float): The input number to add 10 to.

    Returns:
        float: The output number

    Notes:
        This function does this mathematically:.

        .. math::

            \\alpha =& \\beta +1, \\quad \\text{where} \\\\
            \\beta =& \\text{input parameter} \\\\
            \\alpha =& \\text{output} \\\\

        Here is a picture of a banana for your amusement:

        .. image:: _static/banana.png

        .. note:: Bananas are very tasty.

        .. warning:: Do not try to eat more than 3 bananas per day!
    """
    return param + 10


def add_one(param):
    return param + 1


def _add_five(param):
    """
    This docstring wont't be parsed in the HTML page
    :param param: The input number 5 is added to
    :return: The output number
    """
    return param + 5
