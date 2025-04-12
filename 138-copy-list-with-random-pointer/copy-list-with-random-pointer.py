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
        # Avoid empty lists
        if not head:
            return None

        # Create a deep copy without links and match each node to its copy        
        curr = head
        copies = defaultdict(Node)
        while curr:
            curr_copy = Node(x=curr.val)
            copies[curr] = curr_copy
            curr = curr.next

        # Add the links
        curr = head
        while curr:
            curr_copy = copies[curr]
            if curr.next:
                curr_copy.next = copies[curr.next]
            if curr.random:
                curr_copy.random = copies[curr.random]
            curr = curr.next

        return copies[head]