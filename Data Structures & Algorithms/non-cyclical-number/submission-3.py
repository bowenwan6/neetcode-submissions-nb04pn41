class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num not in seen:
            seen.add(num)
            num = self.nextHappy(num)
            if num == 1:
                return True
        return False

    def nextHappy(self, num):
        tot = 0
        while num != 0:
            dig = num % 10
            dig **= 2
            tot += dig
            num //= 10
        return tot
            