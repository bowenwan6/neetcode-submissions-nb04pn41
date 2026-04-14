class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len_d = len(digits)
        inc_next = 1
        for i in range(len_d - 1, -1, -1):
            if inc_next == 0:
                break
            cur = digits[i] + 1
            if cur > 9:
                cur = 0
                digits[i] = cur
            else:
                digits[i] = cur
                inc_next = 0
        if inc_next == 1:
            digits.insert(0, 1)
        return digits
            