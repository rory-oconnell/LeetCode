# 17. Letter Combinations of a Phone Number (Medium)

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case
        if not digits:
            return []
        
        # Create a dictionary of all possible letters for each digit
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        def backtrack(combination, next_digits):
            if not next_digits:

                # All digits are processed, so add the combination to the output
                res.append(combination)
                return
            
            # Iterate over all letters which map the next available digit
            for letter in phone[next_digits[0]]:

                # Append the current letter to the combination and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])

        # Call the backtrack function with an empty string and the input digits
        backtrack("", digits)
        return res
    
# Example usage
digits = "23"
print(Solution().letterCombinations(digits))

# The goal is to produce the following output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]