class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:  # 注意这里是 <，当 l == r 时循环结束，找到目标
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                # 最小值肯定在 m 的右边
                l = m + 1
            else:
                # 最小值在 m 的左边，或者就是 m 本身
                r = m
                
        return nums[l]