"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        linearSeq = { None : None }

        cur = head
        while cur:
            copy = Node(cur.val)
            linearSeq[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = linearSeq[cur]
            copy.next = linearSeq[cur.next]
            copy.random = linearSeq[cur.random]
            cur = cur.next

        return linearSeq[head]