class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None

class Solution:
    def  hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = head
        ptr2 = head
        while ptr2 != None:
            ptr1 = ptr1.next
            if ptr2.next != None:
                ptr2 = ptr2.next.next
            if ptr1 == ptr2:
                return True
        return False
