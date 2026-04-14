class Solution:
    def hammingWeight(self, n: int) -> int:
        n_str = str(bin(n))
        tt = 0
        for num in n_str:
            if num == '1':
                tt += 1
        return tt