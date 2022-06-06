# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        pointer_a = headA
        pointer_b = headB
        
        while pointer_a is not pointer_b:
            pointer_a = pointer_a.next if pointer_a is not None else headB
            pointer_b = pointer_b.next if pointer_b is not None else headA
            
        return pointer_a 
