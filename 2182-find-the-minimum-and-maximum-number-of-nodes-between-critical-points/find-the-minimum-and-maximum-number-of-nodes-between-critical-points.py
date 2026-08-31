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
        
        first = -1
        last = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        index = 1
        
        while curr.next:
            # Check if current node is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):
                
                if first == -1:
                    # First critical point
                    first = index
                    last = index
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, index - last)
                    last = index
            
            prev = curr
            curr = curr.next
            index += 1
        
        # Less than two critical points
        if first == -1 or first == last:
            return [-1, -1]
        
        # Maximum distance
        max_dist = last - first
        
        return [min_dist, max_dist]