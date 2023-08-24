def spiralTraverse(array):
    if not array:
        return []

    result = []
    top, bottom, left, right = 0, len(array) - 1, 0, len(array[0]) - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):   # Move right
            result.append(array[top][j])
        for i in range(top + 1, bottom + 1):   # Move down
            result.append(array[i][right])
        
        # Only perform left and upward traversal if there are still rows or columns left
        if top < bottom:
            for j in range(right - 1, left - 1, -1):   # Move left
                result.append(array[bottom][j])
        if left < right:
            for i in range(bottom - 1, top, -1):   # Move up
                result.append(array[i][left])
                
        # Update boundaries
        top += 1
        bottom -= 1
        left += 1
        right -= 1

    return result

