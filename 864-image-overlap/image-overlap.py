class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        
        points1 = []
        points2 = []
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))
                if img2[i][j] == 1:
                    points2.append((i, j))
        
        count = {}
        
        for x1, y1 in points1:
            for x2, y2 in points2:
                shift = (x2 - x1, y2 - y1)
                count[shift] = count.get(shift, 0) + 1
        
        return max(count.values()) if count else 0