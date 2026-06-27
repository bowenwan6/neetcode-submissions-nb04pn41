class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        candidates.sort()
        def dfs(start, comboSum):
            if comboSum == target:
                res.append(combo.copy())
                return
            if comboSum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                combo.append(candidates[i])
                dfs(i+1, comboSum + candidates[i])
                combo.pop()
        dfs(0, 0)
        return res