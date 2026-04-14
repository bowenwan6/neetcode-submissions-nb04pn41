class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        cur_streak = 1
        longest = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                cur_streak += 1
            else:
                longest = max(longest, cur_streak)
                cur_streak = 1
            
        longest = max(longest, cur_streak)
        return longest