class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> counterS;
        unordered_map<char, int> counterT;

        for (char c : s) {
            counterS[c]++;
        }

        for (char c : t) {
            counterT[c]++;
        }

        return counterT == counterS;
    }
};
