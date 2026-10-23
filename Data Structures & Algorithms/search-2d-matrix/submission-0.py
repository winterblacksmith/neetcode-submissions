class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        for r in range(ROWS):
            if target >= matrix[r][0] and target <= matrix[r][-1]:
                if target in matrix[r]:
                    return True
            else:
                continue
        return False