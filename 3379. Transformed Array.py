class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n):
            target_index = (i + nums[i]) % n
            result.append(nums[target_index])
            
        return result
