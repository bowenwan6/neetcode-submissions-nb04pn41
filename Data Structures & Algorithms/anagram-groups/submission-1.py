class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        classified = defaultdict(list)
        for s in strs:
            group = ''.join(sorted(s))
            classified[group].append(s)
        return classified.values()
        