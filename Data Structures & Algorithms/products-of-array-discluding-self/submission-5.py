class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        f, res = 1, [1] * len(nums)
        for i in range(len(nums)):
            res[i] = f
            f *= nums[i]
        
        b = 1
        for i in range(len(nums) - 1, -1, - 1):
            res[i] *= b
            b *= nums[i]
        return res