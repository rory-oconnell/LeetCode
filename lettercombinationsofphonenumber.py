# 17. Letter Combinations of a Phone Number (Medium)

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case
        if not digits:
            return []
        
        # Create a dictionary of all possible letters for each digit
        phone = {"2": "abc", 
                 "3": "def", 
                 "4": "ghi", 
                 "5": "jkl", 
                 "6": "mno", 
                 "7": "pqrs", 
                 "8": "tuv", 
                 "9": "wxyz"}
                 
        res = []
        
        def backtrack(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return
            
            for letter in phone[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return res
    
# Example usage
digits = "23"
print(Solution().letterCombinations(digits))

# The goal is to produce the following output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]