import math
class MinStack:

    def __init__(self):
        self.vals = []
        

    def push(self, val: int) -> None:
        self.vals.append(val)
        

    def pop(self) -> None:
        del self.vals[-1]
        

    def top(self) -> int:
        return self.vals[-1]
        

    def getMin(self) -> int:
        min_num = math.inf
        for val in self.vals:
            min_num = min(val, min_num)
        return min_num 
        
