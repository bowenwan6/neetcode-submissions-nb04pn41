class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        complete = [i for i in range(n + 1)]
        rem = list(set(complete) - set(nums))
        return rem[0]