class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        def happying(num: int):
            num_S = str(num)
            t = 0
            for c in num_S:
                t += int(c)**2
            return t
        
        num = n
        while num not in seen and num != 1:
            seen.append(num)
            num = happying(num)


        if num == 1:
            return True
        else:
            return False

            