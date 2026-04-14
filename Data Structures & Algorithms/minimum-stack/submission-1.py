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
        temp = []
        mini = self.vals[-1]
        while len(self.vals):
            mini = min(mini, self.vals[-1])
            temp.append(self.vals.pop())
        while len(temp):
            self.vals.append(temp.pop())
        return mini
        
