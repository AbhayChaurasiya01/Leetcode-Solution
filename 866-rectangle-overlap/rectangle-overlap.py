class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        return (rec1[0] < rec2[2] and
                rec1[2] > rec2[0] and
                rec1[1] < rec2[3] and
                rec1[3] > rec2[1])