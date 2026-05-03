class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1

        while l < h:
            m = (h + l) // 2
            print(l, m, h)
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m
        return nums[l]