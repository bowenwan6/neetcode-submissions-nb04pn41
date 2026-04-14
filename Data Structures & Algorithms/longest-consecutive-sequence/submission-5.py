class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        longest = 1
        curr = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1
        longest = max(longest, curr)
        return longest
