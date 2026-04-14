class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case
        if not nums:
            return 0
        
        # Create a sorted, *unique* list of numbers
        sorted_nums = sorted(set(nums))
        
        longest = 1
        current_streak = 1
        
        # Traverse the sorted list
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                # Continue the streak
                current_streak += 1
            else:
                # Streak ended; update longest if necessary
                longest = max(longest, current_streak)
                current_streak = 1
        
        # Final check for the last streak
        longest = max(longest, current_streak)
        
        return longest
