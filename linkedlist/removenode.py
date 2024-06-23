# Remove Node From End of Linked List
# Solved 
# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

# Input: head = [1,2,3,4], n = 2

# Output: [1,2,4] 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) 
        l, r = dummy, head 

        while n > 0:
            r = r.next 
            n -= 1 
        while r:
            l = l.next 
            r = r.next 

        l.next = l.next.next 
        return dummy.next 