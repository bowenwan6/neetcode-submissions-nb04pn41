class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [None] * len(temperatures)
        for i, temp in enumerate(temperatures):
            for j in range(1, len(temperatures) - i):
                if temp < temperatures[i + j]:
                    res[i] = j
                    break
        res = [0 if x is None else x for x in res]
        return res
                
        