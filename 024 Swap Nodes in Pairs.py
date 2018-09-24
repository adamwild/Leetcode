# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sp2 (self, head, prev):
        if head == None or head.next == None:
            return head
        else:
            n3 = head.next.next
            n2 = head.next
            n2.next = head
            head.next = n3
            prev.next = n2
            self.sp2(n3, head)
        return n2
    
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            n3 = head.next.next
            n2 = head.next
            n2.next = head
            head.next = n3
            self.sp2(n3, head)
        return n2
