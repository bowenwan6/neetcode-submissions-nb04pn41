# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        nums = []
        while cur:
            nums.append(cur)
            cur = cur.next
        numRemove = len(nums) - n
        if numRemove == 0:
            return head.next
        nums[numRemove - 1].next = nums[numRemove].next
        return head