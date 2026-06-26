class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[List[int]]]:
        res = []
        combo = []
        
        # 1. Sort to bring duplicates next to each other
        candidates.sort()

        def dfs(start_idx, current_sum):
            if current_sum == target:
                res.append(combo.copy())
                return
            if current_sum > target:
                return

            for i in range(start_idx, len(candidates)):
                # 2. Skip duplicates at the same decision level
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include candidates[i]
                combo.append(candidates[i])
                # Move to i + 1 because each element can only be used once
                dfs(i + 1, current_sum + candidates[i])
                # Backtrack
                combo.pop()

        dfs(0, 0)
        return res