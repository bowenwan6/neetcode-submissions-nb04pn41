class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2)):
            curr = s2[i : i + len(s1)]
            curr = sorted(curr)
            if curr == s1:
                return True
        return False
