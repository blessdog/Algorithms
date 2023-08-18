'''
Write a func that takes in two non-empty arrays of ints, finds the pair of numbers 
(one from each array) whose absolute diff is closest to zero, and returns an array containing 
these 2 numbers, with the number from the first array in the first position. 

'''
array_one = [-1, 5, 10, 20, 28, 3]
array_two = [26, 134, 135, 15, 17]

outPut = [28, 26]

def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()

    idx1, idx2 = 0, 0
    smallest, current = float('inf'), float('inf')
    smallestPair = []

    while idx1 < len(array1) and idx2 < len(array2):
        firstNum = array1[idx1]
        secondNum = array2[idx2]





