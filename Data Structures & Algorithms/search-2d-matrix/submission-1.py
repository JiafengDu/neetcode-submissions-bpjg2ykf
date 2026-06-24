class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_top, row_bottom = 0, len(matrix)-1
        
        while row_top <= row_bottom:
            mid = row_top + (row_bottom-row_top)//2
            if target > matrix[mid][-1]:
                row_top = mid+1
            elif target < matrix[mid][0]:
                row_bottom = mid-1
            else:
                break
        
        if row_top > row_bottom:
            return False
        
        left, right = 0, len(matrix[0])-1
        while left <= right:
            col_mid = left + (right - left) //2
            if target > matrix[mid][col_mid]:
                left = col_mid+1
            elif target < matrix[mid][col_mid]:
                right = col_mid-1
            else:
                return True

        return False    