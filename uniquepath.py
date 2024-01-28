class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(1, m):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
    
# Example usage
m = 3
n = 7
print(Solution().uniquePaths(m, n)) # 28