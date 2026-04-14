class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sizeN = len(nums)
        for i in range(sizeN):
            for j in range(i+1, sizeN):
                for k in range(j+1, sizeN):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                        res.add(triplet)
        return [list(x) for x in res]
                    
