'''
Write a function that takes in an array of integers and returns a booly representing 
weather the array is monotonic. 
An array is monotonic if its elements, from left to right, are entirely non-increasing or entirely 
non-decreasing. 
Non-increasing elements arent necessarily exclusivly decreasing; they simply dont increase. Similarly 
with non-decreasing. 
Note that empty arrays and arrays of one element are monotonic. 
'''
'''
To determine if an array is monotonic, we can take the following approach:

1. If the array has one or zero elements, return True.
2. Scan the array to determine the direction: increasing, decreasing, or equal.
3. Once the direction is determined, scan the rest of the array to see if the direction ever changes.
'''



def isMonotonic(array):
    # Handle arrays of size 0 or 1
    if len(array) <= 1:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array))

