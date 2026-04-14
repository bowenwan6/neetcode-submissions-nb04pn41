class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = (32 - len(bin(n)[2:])) * "0" + bin(n)[2:]
        rev_n = bin_n[::-1]
        int_rev = int(rev_n, 2)
        return int_rev