# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left_node, right_node = head, head
        left_anchor = None

        while right > 1:
            if left > 1:
                left_anchor = left_node
                left_node = left_node.next
            right_node = right_node.next
            right -= 1
            left -= 1
        right_anchor =  right_node.next
        

        curr, prev = left_node, None
        while curr != right_anchor:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        if left_anchor:
            left_anchor.next = right_node
        else:
            head = right_node

        left_node.next = right_anchor

        return head