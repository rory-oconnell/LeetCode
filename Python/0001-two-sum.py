nums = [2,7,11,15]
target = 9

def twosum(nums, target):
    prevmap = {} # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevmap:
            return [prevmap[diff], i]
        prevmap[n] = i


if __name__ == "__main__":
    answer = twosum(nums, target)
    

