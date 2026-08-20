# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            kth = self.getK(prev, k)
            if not kth:
                break
            nextg = kth.next

            prevr, curr = kth.next, prev.next
            while curr != nextg:
                temp = curr.next
                curr.next = prevr
                prevr = curr
                curr = temp
            
            temp = prev.next
            prev.next = kth
            prev = temp
        return dummy.next

    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
