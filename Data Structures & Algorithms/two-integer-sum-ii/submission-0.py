class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start from two ends
        # if sum is bigger than target, decrease right pointer using binary
        # if sum == target: return pointers
        # else: (sum smaller than target), increase left pointer using binary
        left, right = 0, len(numbers)-1
        while left<right:
            current = numbers[left]+numbers[right]
            if target > current:
                left += 1 # maybe update using binary?
            elif target == current:
                return [left+1, right+1]
            else:
                right -= 1 # maybe update using binary?

        return -1
            