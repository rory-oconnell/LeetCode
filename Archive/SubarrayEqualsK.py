# Brute Force Approach
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#
#         subarrays = 0
#         total = 0
#
#         for i in range(0, len(nums), 1):
#             total = 0
#             for j in range(i, len(nums), 1):
#                 total += nums[j]
#                 if total == k:
#                     subarrays += 1
#         return subarrays

nums = [1,-1,0]
k = 0
d = {0: 1}

sums = 0
count = 0

for i in range(len(nums)):
    sums += nums[i]

    if sums - k in d:
        count += d[sums - k]

    if sums in d:
        d[sums] += 1

    else:
        d[sums] = 1

print(count)
