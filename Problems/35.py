# nums = [1,3,5,6]
nums = [1]
# target = 2
# target = 3
target = 7

returnVal = 0
for i in range(len(nums)):
    if nums[i] == target:
        returnVal = i
        break
    elif i == len(nums)-1 and nums[i] != target:
        if nums[i] > target:
            returnVal = i
        elif nums[i] < target:
            returnVal = i+1
        break
    elif nums[i] > target:
        returnVal = i
        break
print(returnVal) 