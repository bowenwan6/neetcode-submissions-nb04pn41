class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        total_len = len(numbers)
        for i in range(total_len):
            a = numbers[i]
            expected_b = target - a
            for j in range(i, total_len):
                if expected_b == numbers[j]:
                    return [i+1, j+1]
                    continue