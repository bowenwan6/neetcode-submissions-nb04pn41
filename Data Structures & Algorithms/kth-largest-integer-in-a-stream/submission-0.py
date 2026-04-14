class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.nums = nums
        

    def add(self, val: int) -> int:
        nums = self.nums
        for i in range(len(nums)):
            if nums[i] < val:
                continue
            else:
                nums.insert(i, val)
                break
        else:
            nums.append(val)
        self.nums = nums
        k = self.k
        return nums[-k]