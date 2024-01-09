needle = "cd"
haystack = "abcdefg"

if needle == haystack:
    print("Needle Found at index 0")
i = 0
j = len(needle)
while j <= len(haystack):
    currentNeedle = haystack[i:j]
    if currentNeedle == needle:
        print("Needle Found at index", i)
    i += 1
    j += 1
print("Needle not found")