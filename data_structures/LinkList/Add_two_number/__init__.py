from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        tail_node = result
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_value, l1 = (l1.val, l1.next) if l1 else (0, None)
            l2_value, l2 = (l2.val, l2.next) if l2 else (0, None)

            total_sum = l1_value + l2_value + carry
            carry = total_sum // 10
            value = total_sum % 10

            temp_node = ListNode(value)
            tail_node.next = temp_node
            tail_node = temp_node
        result = result.next
        return result

if __name__ == "__main__":
  l1 = ListNode(9)
  l1.next = ListNode(9)
  l1.next.next = ListNode(9)
  l1.next.next.next = ListNode(9)
  l1.next.next.next.next = ListNode(9)
  l1.next.next.next.next.next = ListNode(9)
  l1.next.next.next.next.next.next = ListNode(9)
  
  l2 = ListNode(9)
  l2.next = ListNode(9)
  l2.next.next = ListNode(9)
  l2.next.next.next = ListNode(9)
  
  sol = Solution()
  result = sol.addTwoNumbers(l1, l2)
  
  # result [8,9,9,9,0,0,0,1]
