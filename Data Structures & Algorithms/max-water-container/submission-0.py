class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                maxVol = max(maxVol, min(heights[i], heights[j])*(j-i))
        return maxVol