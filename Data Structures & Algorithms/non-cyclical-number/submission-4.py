class Solution:
    def isHappy(self, n: int) -> bool:
        def nextHappy(num):
            res = 0
            cur = num
            while cur != 0:
                res += (cur % 10) ** 2
                cur = cur // 10
            return res

        slow, fast = n, nextHappy(n)
        while slow != fast:
            slow = nextHappy(slow)
            fast = nextHappy(fast)
            fast = nextHappy(fast)
        return True if fast == 1 else False
    
