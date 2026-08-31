# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        prev = head
        curr = head.next
        idx = 2
        while curr.next:
            is_maxima = curr.val > prev.val and curr.val > curr.next.val
            is_minima = curr.val < prev.val and curr.val < curr.next.val
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = idx
                else:
                    min_dist = min(min_dist, idx - prev_cp)
                prev_cp = idx
            prev = curr
            curr = curr.next
            idx += 1
        if first_cp == -1 or first_cp == prev_cp:
            return [-1, -1]
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]
        