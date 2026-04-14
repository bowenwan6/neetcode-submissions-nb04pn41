from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        classified = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            classified[key].append(s)
        return list(classified.values())
