class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (string s : strs) {
            res += to_string(s.size()) + ":" + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        int l = 0;
        vector<string> res;
        while (l < s.size()) {
            int r = l;
            while (s[r] != ':') {
                r++;
            }
            int len = stoi(s.substr(l, r - l));
            l = r + 1;
            r = l + len;
            res.push_back(s.substr(l, len));
            l = r;
        }
        return res;
    }
};
