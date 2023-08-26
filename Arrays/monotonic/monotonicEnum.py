from enum import Enum, auto

class Direction(Enum):
    INCREASING = auto()
    DECREASING = auto()
    NEUTRAL = auto()

def isMonotonic(array):
    if len(array) <= 1:
        return True

    # Determine the initial direction
    direction = Direction.NEUTRAL
    if array[1] > array[0]:
        direction = Direction.INCREASING
    elif array[1] < array[0]:
        direction = Direction.DECREASING

    for i in range(2, len(array)):
        if direction == Direction.NEUTRAL:
            if array[i] > array[i-1]:
                direction = Direction.INCREASING
            elif array[i] < array[i-1]:
                direction = Direction.DECREASING
            continue

        # If direction changes, return False
        if breaksDirection(direction, array[i-1], array[i]):
            return False
    
    return True

def breaksDirection(direction, previousInt, currentInt):
    if direction == Direction.INCREASING:
        return currentInt < previousInt
    elif direction == Direction.DECREASING:
        return currentInt > previousInt
    return False

