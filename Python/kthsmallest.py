# Input: arr[] = {7, 10, 4, 3, 20, 15}
#        k = 3
# Output: 7
#
# Input: arr[] = {7, 10, 4, 3, 20, 15}
#       k = 4
# Output: 10

arr = {7, 10, 4, 3, 20, 15}
k = 3
answer = 7

sorted = sorted(arr)

print(sorted[k-1])