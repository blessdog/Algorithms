'''
Write a func that takes in two non-empty arrays of ints, finds the pair of numbers 
(one from each array) whose absolute diff is closest to zero, and returns an array containing 
these 2 numbers, with the number from the first array in the first position. 

'''

def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()

    idx1, idx2 = 0, 0
    smallest, current = float('inf'), float('inf')
    smallestPair = []

    while idx1 < len(array1) and idx2 < len(array2):
        firstNum = array1[idx1]
        secondNum = array2[idx2]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idx1 += 1

        elif secondNum < firstNum:
            current = firstNum - secondNum
            idx2 += 1

        else:
            return [firstNum, secondNum]
        
        if current < smallest: 
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair





