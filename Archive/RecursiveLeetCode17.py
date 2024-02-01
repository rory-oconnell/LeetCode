from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []

        def helperFunction(index, currentString):
            if index == len(digits):
                combinations.append(currentString)
            else:
                for letter in phone[digits[index]]:
                    helperFunction(index + 1, currentString + letter)
        
        helperFunction(0, '')

        return combinations

# Example usage:
    
digits = "23"
solution = Solution()
print(solution.letterCombinations(digits))