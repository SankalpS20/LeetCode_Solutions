class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def find_max_in_column(mat, mid_col):
            max_row = 0
            for row in range(len(mat)):
                if mat[row][mid_col] > mat[max_row][mid_col]:
                    max_row = row
            return max_row

        rows, cols = len(mat), len(mat[0])
        left, right = 0, cols - 1
        
        while left <= right:
            mid_col = left + (right - left) // 2
            max_row = find_max_in_column(mat, mid_col)
            
            if (mid_col == 0 or mat[max_row][mid_col] > mat[max_row][mid_col - 1]) and \
               (mid_col == cols - 1 or mat[max_row][mid_col] > mat[max_row][mid_col + 1]):
                return [max_row, mid_col]
            elif mid_col > 0 and mat[max_row][mid_col] < mat[max_row][mid_col - 1]:
                right = mid_col - 1
            else:
                left = mid_col + 1
        
        return []