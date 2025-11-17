class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1  # índice do último 1 encontrado
        
        for i, val in enumerate(nums):
            if val == 1:
                if last != -1 and (i - last - 1) < k:
                    return False
                last = i
        
        return True
