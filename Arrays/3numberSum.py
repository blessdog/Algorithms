'''
Write a function that takes in a non-empty array of distinct integers and an interger representing a target sum. 
The function should find all the triplets in the array that sum up to thye target sum and return a two-dimensional array of all these triplets. The number in each triplet should be ordered in ascending order, and the tripl,ets themselves should be ordered in ascending order with respect to the numbers they hold.

If no three numbers sum up to the target sum, the function should return and empty array.

----------------------------------------
----------------------------------------

Sample Input

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

Sample Output
[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

'''

def three_sum(nums, target):
    nums.sort()
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplets

# Example usage
nums = [12, 3, 1, 2, -6, 5, -8, 6]
target_sum = 0
result = three_sum(nums, target_sum)
print(result)  # Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]


'''
1) 
First, sort the array.
2) 
Use a for-loop to iterate over the array. Let's call the current number 'a'.
3) 
Use two pointers, one starting from the next number after 'a', and the other starting from the end of the array.
4)
For each 'a', check the sum of the numbers at the two pointers. If the sum is greater than the target minus 'a', move the end pointer backward. If the sum is less than the target minus 'a', move the starting pointer forward. If the sum is equal to the target minus 'a', add the triplet to the result list.
5)
Continue this process until the two pointers meet.
6)
After processing the triplet for one 'a', move to the next 'a' in the array and repeat the process.
'''

def 3_number_sum(array, target_sum):
    array.sort()
    triplets = []

    for i in range(len(array) - 1):
        left += 1
        right  = len(array) -1

        while left < right

