from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isListDuplicate(nums):
            seen = set()
            for num in nums:
                if num != '.' and num in seen:
                    return True
                seen.add(num)
            return False

        def column(x, i):
            return [row[i] for row in x]

        def block(x, i):
            temp = []
            row = (i // 3) * 3
            col = (i % 3) * 3
            for k in range(3):
                for q in range(3):
                    temp.append(x[row + k][col + q])
            return temp

        for i in range(9):
            if (isListDuplicate(board[i]) or
                isListDuplicate(column(board, i)) or
                isListDuplicate(block(board, i))):
                return False
        
        return True  # Only return True if all checks pass
