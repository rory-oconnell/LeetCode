nums = [1,2,2,3,3,3]
k = 2
# Output: [1,2] 

# Count the frequency of each number.
freqs = {}
for num in nums:
    if num not in freqs:
        freqs[num] = 0
    freqs[num] += 1

# freqs = {1: 3, 2: 2, 3: 1}

