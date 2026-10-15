class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=[]
        for i in range(len(nums)):
            
            for j in range(i,len(nums)):
                sub=nums[i:j+1]
                r.append(len(set(sub))**2)
        return sum(r)

        