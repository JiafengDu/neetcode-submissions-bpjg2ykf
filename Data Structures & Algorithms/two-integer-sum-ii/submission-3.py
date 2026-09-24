class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            left, right = i+1, n-1
            need = target - numbers[i]
            while left <= right:
                mid = left + (right-left)//2

                if numbers[mid] == need:
                    return [i+1, mid+1]
                elif numbers[mid] < need:
                    left = mid + 1
                else:
                    right = mid - 1
        return []
