class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = [c for c in s]
        longest = 0
        for i in range(len(st)):
            word = []
            for j in range(i, len(st)):
                if st[j] not in word:
                    word.append(st[j])
                else:
                    break
            currLen = len(word)
            longest = max(longest, currLen)
        return longest
