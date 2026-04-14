class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seq = {}
        for i, num in enumerate(nums):
            seq[num] = i
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seq and seq[diff] != i:
                return [i, seq[diff]]