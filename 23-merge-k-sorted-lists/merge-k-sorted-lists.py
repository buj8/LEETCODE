# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        current = ListNode()
        nodezero = ListNode(next=current)

        lists = [i for i in lists if i]

        while len(lists)>0:
            current_min = float('inf')
            next_node = -1
            for i in range(len(lists)):
                if lists[i].val <= current_min:
                    current_min = lists[i].val
                    next_node = i
            newnode = ListNode(val=current_min)
            current.next = newnode
            current = newnode
            lists[next_node] = lists[next_node].next
            if lists[next_node] == None:
                lists.pop(next_node) 

        return nodezero.next.next
                
        