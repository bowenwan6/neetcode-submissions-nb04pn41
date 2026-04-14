class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) <= 1:
            return True if target in matrix[0] else False
        for i in range(1, len(matrix)):
            if matrix[i][0] > target:
                for j in range(len(matrix[0])):
                    if matrix[i-1][j] == target:
                        return True
            elif matrix[i][0] == target:
                return True
            else:
                pass
        return True if target in matrix[-1] else False
        return False