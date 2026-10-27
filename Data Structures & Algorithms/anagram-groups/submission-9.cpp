class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        for (const auto& s : strs) {
            vector<int> bucket(26);
            for (char c : s) {
                bucket[c - 'a']++;
            }
            string key = to_string(bucket[0]);
            for (int i = 1; i < 26; i++) {
                key += ',' + to_string(bucket[i]);
            }
            anagrams[key].push_back(s);
        }

        vector<vector<string>> res;
        for (const auto& p : anagrams) {
            res.push_back(p.second);
        }
        return res;
    }
};
