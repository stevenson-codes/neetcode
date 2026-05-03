class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, water = 0, len(height) - 1, 0
        lmax, rmax = height[l], height[r]
        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)
            water += lmax - height[l] + rmax - height[r]
            if lmax < rmax:
                l += 1
            else:
                r -= 1

        return water