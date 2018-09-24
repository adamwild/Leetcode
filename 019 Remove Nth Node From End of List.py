# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        by_node = head
        cpt = n
        curr_node = head
        if head.next is None and n==1:
            return None
        while curr_node is not None:
            if cpt == -1:
                by_node = by_node.next
            else:
                cpt -= 1
            curr_node = curr_node.next
        if cpt == 0:
            head = head.next
        else :
            by_node.next = by_node.next.next
        return head
