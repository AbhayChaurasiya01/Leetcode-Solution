class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: count frequencies
        cnt = collections.Counter(nums)
        
        # Step 2: collect those numbers whose frequency == 2
        result = [num for num, freq in cnt.items() if freq == 2]
        
        return result