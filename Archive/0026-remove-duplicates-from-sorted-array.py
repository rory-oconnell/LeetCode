nums = [1, 2, 3, 1]

hashset = set()
for i in nums:
    if i not in hashset:
        hashset.add(i)
    else:
        print("duplicate")