__author__ = 'MacPu'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 != None or l2 != None:
            val = carry
            if l1.val != None:
                val += l1.val
                l1 = l1.next

            if l2.val != None:
                val += l2.val
                l2 = l2.next

            current.next , carry = ListNode(val % 10) , val /10
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)
