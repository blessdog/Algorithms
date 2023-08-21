'''
Write a function that takes in an array of integers and returns a booly representing 
weather the array is monotonic. 
An array is monotonic if its elements, from left to right, are entirely non-increasing or entirely 
non-decreasing. 
Non-increasing elements arent necessarily exclusivly decreasing; they simply dont increase. Similarly 
with non-decreasing. 
Note that empty arrays and arrays of one element are monotonic. 
'''

def isMonotonic(array):
    # Handle arrays of size 0 or 1
    if len(array) <= 1:
        return True

    # Determine the direction
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        # If direction hasn't been set, find the next difference
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue

        # If direction changes, return False
        if hasDirectionChanged(direction, array[i - 1], array[i]):
            return False

    return True

def hasDirectionChanged(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0

