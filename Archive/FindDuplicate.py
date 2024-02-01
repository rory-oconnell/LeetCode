def findDuplicate(nums):
    # Phase 1: Finding the intersection point of the two runners.
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Finding the "entrance" to the cycle.
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Example usage:
array = [3, 1, 3, 4, 2]
print(findDuplicate(array))  # Outputs 3, as 3 is the duplicate
