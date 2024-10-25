# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        
        while curr:
            temp = curr.next  # Save the next node
            curr.next = prev  # Reverse the link
            prev = curr       # Move prev to the current node
            curr = temp       # Move to the next node
        
        return prev  # prev will be the new head of the reversed list
