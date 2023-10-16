needle = "cd"
haystack = "abcdefg"

print("Haystack: ", haystack)
print("Needle: ", needle)

# delcaring the thing we will use to compare strings
checkList = []
m = 0

# if the needle is bigger than the haystack
if len(haystack) < len(needle):
    print("Needle not found")

# first iteration of filling the thing to be checked
for i in range(len(needle)):
    checkList.append(haystack[i])

# turning the checklist into a string for comparison
checkString = "".join(checkList)
print(checkString)

if checkString == needle:
    print("Needle Found at index", m)

i = i+1
m = m+1

if i >= len(haystack):
    print("Needle not found")


while checkString != needle:
    checkList.remove(checkList[0])
    checkList.append(haystack[i])
    checkString = "".join(checkList)
    if checkString == needle:
        print("Needle Found at index", m)
    print(checkString)
    print(i)
    i = i + 1
    m = m + 1
    if i >= len(haystack):
        print("Needle not found")
