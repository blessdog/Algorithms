def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False

        # Check if both flags are False and break if so
        if not isNonIncreasing and not isNonDecreasing:
            break

    return isNonIncreasing or isNonDecreasing
