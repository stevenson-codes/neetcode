class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> count;

        for (int num : nums) {
            if (count.count(num)) {
                return true;
            }
            count.insert(num);
        }
        return false;
    }
};