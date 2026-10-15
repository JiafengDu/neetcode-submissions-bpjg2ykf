class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # (0,0)->(0,1)->(0,2)->(1,2)->(2,2)->(2,1)->(2,0)->(1,0)->(1,1)
        # n = len(matrix)
        # boundery = n
        # while i < n^2:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        top, bottom, left, right = 0, m, 0, n

        while left < right and top < bottom:
            for col in range(left, right):
                res.append(matrix[top][col])
            top += 1
            
            for row in range(top, bottom):
                res.append(matrix[row][right-1])
            right -= 1

            if not (left<right and top<bottom):
                break
            
            for col in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][col])
            bottom -= 1

            for row in range(bottom-1, top-1, -1):
                res.append(matrix[row][left])
            left += 1
        
        return res