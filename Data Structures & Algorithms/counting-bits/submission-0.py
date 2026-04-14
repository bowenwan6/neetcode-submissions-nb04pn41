class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            r = 0
            for i in range(32):
                if (1 << i) & num:
                    r += 1
            res.append(r)
        return res
                