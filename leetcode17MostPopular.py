from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_mapping = { '2': "abc",'3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
        combinations: List[str] = []

        if len(digits) == 0:
            return combinations

        elif len(digits) == 1:
            for i in range(len(phone_mapping[digits[0]])):
                combinations.append(phone_mapping[digits[0]][i])

        elif len(digits) == 2:
            for i in range(len(phone_mapping[digits[0]])):
                for j in range(len(phone_mapping[digits[1]])):
                    combinations.append(phone_mapping[digits[0]][i] + phone_mapping[digits[1]][j])

        elif len(digits) == 3:
            for i in range(len(phone_mapping[digits[0]])):
                for j in range(len(phone_mapping[digits[1]])):
                    for k in range(len(phone_mapping[digits[2]])):
                        combinations.append(phone_mapping[digits[0]][i] + phone_mapping[digits[1]][j] + phone_mapping[digits[2]][k])

        elif len(digits) == 4:

            for i in range(len(phone_mapping[digits[0]])):
                for j in range(len(phone_mapping[digits[1]])):
                    for k in range(len(phone_mapping[digits[2]])):
                        for l in range(len(phone_mapping[digits[3]])):
                            combinations.append(phone_mapping[digits[0]][i] + phone_mapping[digits[1]][j] + phone_mapping[digits[2]][k] + phone_mapping[digits[3]][l])
        return combinations