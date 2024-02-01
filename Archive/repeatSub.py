
def lengthOfLongestSubstring(s):
    letterDict = {}
    currStr = 0
    longestStr = 0
    for i in range(0, len(s), 1):
        if s[i] not in letterDict:
            # the dictionary stores the position of the encountered rep
            letterDict[s[i]] = i
            currStr += 1
            if currStr > longestStr:
                longestStr = currStr
        elif s[i] in letterDict:
            i = letterDict[s[i]] + 1
            letterDict.clear()
            letterDict[s[i]] = i
            currStr = 1
    return longestStr

# store the index of the repeating character
# reset the for loop to start after the repeated character

s = "dvdf"
longestString = lengthOfLongestSubstring(s)
print(longestString)