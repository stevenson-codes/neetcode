class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minP = prices[0];
        int profit = 0;

        for (const int p : prices) {
            minP = min(minP, p);
            profit = max(profit, p - minP);
        }
        return profit;
    }
};
