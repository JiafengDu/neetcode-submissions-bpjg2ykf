class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix)-1
        target_row = -1

        while up <= down:
            mid = up + (down-up)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                target_row = mid
                break
            elif target < matrix[mid][0]:
                down = mid-1
            else:
                up = mid+1
        
        if target_row == -1:
            return False
        
        left, right = 0, len(matrix[0])-1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[target_row][mid]==target:
                return True
            elif matrix[target_row][mid]>target:
                right = mid-1
            else:
                left = mid+1
        return False