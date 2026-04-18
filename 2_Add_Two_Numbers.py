from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        total = carry = 0
        
        while l1 or l2 or carry :
            
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
    
c1 = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = c1.addTwoNumbers(l1, l2)
print(result.val)  # Output: 7
print(result.next.val)  # Output: 0 
print(result.next.next.val)  # Output: 8