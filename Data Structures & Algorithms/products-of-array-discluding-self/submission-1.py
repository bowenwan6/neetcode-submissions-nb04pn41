class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        res = []
        for num in nums:
            if num:
                prod *= num
            elif num == 0:
                zeros += 1
        if zeros > 1:
            return [0] * (len(nums))
        elif zeros == 1:
            res = [0] * (len(nums))
            zero_idx = nums.index(0)
            res[zero_idx] = prod
        elif zeros == 0:
            for i in range(len(nums)):
                res.append(int(prod/nums[i]))
        return res

        
        