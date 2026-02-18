class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        
        ptr1 = head
        ptr2 = head
        while ptr2.next != None:
            ptr1 = ptr1.next
            if ptr2.next.next != None:
                ptr2 = ptr2.next.next
            else:
                break
        return ptr1

