def strStr(haystack, needle):
    if needle =="":
        return 0
    
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# Example usage
haystack = "sadbutsad"
needle = "sad"
result = strStr(haystack, needle)
print(f"The needle '{needle}' is found in '{haystack}' at index: {result}")
