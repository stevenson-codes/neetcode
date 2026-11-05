class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0; int r = height.size() - 1; int water = 0;
        int lmax = height[l]; int rmax = height[r];

        while (l < r) {
            if (lmax < rmax) {
                l++;
                lmax = max(lmax, height[l]);
                water += lmax - height[l];
            } else {
                r -= 1;
                rmax = max(rmax, height[r]);
                water += rmax - height[r];
            }
        }
        return water;
    }
};
