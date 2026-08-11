class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        numset=set(nums)
        ans=nums[0]

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                break
            ans+=nums[i]
        while ans in numset:
            ans+=1
        return ans