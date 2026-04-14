class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        def calArea(l, r, w):
            return (min(l, r) * w)
        l, r = 0, len(heights) - 1
        while l < r:
            area = calArea(heights[l], heights[r], r-l)
            max_v = max(max_v, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_v