class Solution:
    def findMin(self, nums: List[int]) -> int:
        minN = math.inf
        for num in nums:
            minN = min(num, minN)
        return minN