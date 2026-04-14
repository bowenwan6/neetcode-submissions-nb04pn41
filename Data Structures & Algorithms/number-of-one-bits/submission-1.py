class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bin = bin(n)
        tt = n_bin.count('1')
        return tt