class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        classified = defaultdict(int)
        for num in nums:
            classified[num] += 1
        sorted_nums = sorted(classified.keys(), key= lambda x: classified[x], reverse= True)
        return sorted_nums[:k]