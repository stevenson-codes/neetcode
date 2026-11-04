class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, water = 0, len(height) - 1, 0
        lmax, rmax = height[l], height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                water += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                water += rmax - height[r]
        return water