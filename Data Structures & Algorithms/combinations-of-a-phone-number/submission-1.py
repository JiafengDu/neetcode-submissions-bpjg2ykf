class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # have the mapping
        # backtrack dfs:
        #   if curr is length of digits, append to res
        #   recursive: loop through each char for the digit letter, recursively call dfs with updated curr
        if not digits:
            return []
        digit_to_char = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = [""]

        for digit in digits:
            res = [prefix+char for prefix in res for char in digit_to_char[digit]]

        return res
            