nums = [4,1,2,1,2]

def singleNumber(nums):
    nums.sort()
    i = 0
    while i < len(nums):
        if i == len(nums) - 1:
            return nums[i]
        if nums[i] == nums[i+1]:
            i += 2
        else:
            return nums[i]


if __name__ == "__main__":
    print(singleNumber(nums))


