class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> res;

        for (int i = 0; i < nums.size(); i++) {
            if (res.find(nums[i]) != res.end()){
                return {res[nums[i]], i};
            }
            res.insert({target - nums[i], i});
        }
        return {};
    }
};
