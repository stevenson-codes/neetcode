class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward, backward = [1] * len(nums), [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            forward[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            backward[i] = product 
            product *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(forward[i] * backward[i])
        
        return res
