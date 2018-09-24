# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = l1.val + l2.val
        if val1>=10:
            ret = 1
        else:
            ret = 0
        sol = ListNode(val1%10)
        l1 = l1.next
        l2 = l2.next
        curr_node = sol
        if l1 is None and l2 is None:
            if ret == 1:
                sol.next = ListNode(1)
            return sol
        while l1 is not None or l2 is not None:
            print("Hello")
            if l1 is None:
                v1 = 0
            else:
                v1 = l1.val
            if l2 is None:
                v2 = 0
            else:
                v2 = l2.val
            val = v1+v2+ret
            new_node = ListNode(val%10)
            curr_node.next = new_node
            curr_node = curr_node.next
            if val>=10:
                ret = 1
            else:
                ret = 0
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 is None and l2 is None and ret==1:
                curr_node.next = ListNode(1)
        return sol
