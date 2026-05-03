class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        f, listF = 1, [1] * len(nums)
        print(listF)
        for i in range(len(nums)):
            listF[i] = f
            f *= nums[i]
        
        b, res = 1, [0] * len(nums)
        for i in range(len(nums) - 1, -1, - 1):
            res[i] = b * listF[i]
            b *= nums[i]
        return res