# LeetCode problem 347. Top K Frequent Elements
nums = []

freqs = {}

for num in nums:
    if num not in freqs:
        freqs[num] = 0
    freqs[num] += 1