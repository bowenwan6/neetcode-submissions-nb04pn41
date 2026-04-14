import math
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesH = [-item for item in stones]
        heapq.heapify(stonesH)
        while len(stonesH) > 1:
            x = -heapq.heappop(stonesH)
            y = -heapq.heappop(stonesH)
            rem = abs(x-y)
            if rem > 0:
                heapq.heappush(stonesH, -rem)
        return -stonesH[0] if stonesH else 0  