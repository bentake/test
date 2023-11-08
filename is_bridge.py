"""
    CS5001_5003 Fall 2023 SV
    Lab09
    Gio Ong / Byunghyun Ko
"""


def is_bridge(course):
    ''' Function: is_bridge
            Test whether course is part of the bridge
        Parameters:
            course. a number of a course (without the CS)
        Returns T if the course is 5001, 5002, 5003, 5004, 5005, 5008 or 5009
            or F otherwise
        Raises TypeError if the value of the course is not an integer
    '''
    if not isinstance(course, int):
        print("type error called")
        raise TypeError("course must be an integer")
    valid_crn = [5001, 5002, 5003, 5004, 5005, 5008, 5009]
    if course in valid_crn:
        return True
    else:
        return False
