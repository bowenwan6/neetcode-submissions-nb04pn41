class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alphabetic items from s
        sAlpha = ''.join(x.lower() for x in s if x.isalpha() or x.isnumeric())
        return sAlpha == sAlpha[::-1]
