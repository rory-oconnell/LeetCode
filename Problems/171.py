s = "ZY"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# start_value, stop_value, and step value
for i in range(len(alphabet)-1, -1, -1):
    print(alphabet[i])
    print(ord(alphabet[i]))

# multiplier = 1
# column = 0
# for i in range(len(s)-1, -1, -1):
#     column += (ord(s[i])-64)*multiplier
#     multiplier *= 26
# print(column)
