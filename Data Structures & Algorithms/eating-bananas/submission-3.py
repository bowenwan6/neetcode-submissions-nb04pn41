class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while r >= l:
            k = (l + r) // 2
            totalH = 0
            for pile in piles:
                totalH += math.ceil(pile / k)
            if totalH <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
            
