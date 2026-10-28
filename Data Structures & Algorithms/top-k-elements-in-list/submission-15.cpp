class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        vector<vector<int>> freqs(nums.size() + 1);

        for (int num : nums) counter[num]++;

        for (const auto& p : counter) {
            freqs[p.second].push_back(p.first);
        }

        vector<int> res;
        for (int i = nums.size(); i > 0; i--) {
            for (const auto& num : freqs[i]) {
                res.push_back(num);
                if (res.size() == k) return res;
            }
        }
        return res;
    }
};
