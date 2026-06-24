class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        currentCom = []

        def dfs(i, currentSum):
            if currentSum == target:
                res.append(currentCom.copy())
                return
            if currentSum >= target or i >= len(nums):
                return

            currentCom.append(nums[i])
            dfs(i, currentSum + nums[i])
            currentCom.pop()
            dfs(i + 1, currentSum)

        dfs(0, 0)
        return res
