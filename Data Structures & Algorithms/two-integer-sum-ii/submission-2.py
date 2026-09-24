class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left, right starts at end
        # if sum of left and right is > target, need decrease -> right - 1
        # if sum of left and right < target, need increase -> left + 1
        left, right = 0, len(numbers)-1

        while left < right:
            x = numbers[left]+numbers[right]
            if x > target:
                right -= 1
            elif x < target:
                left += 1 
            else:
                return [left+1, right+1]
        return []