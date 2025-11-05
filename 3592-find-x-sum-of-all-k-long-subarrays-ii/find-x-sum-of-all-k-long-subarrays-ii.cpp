class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();
        vector<long long> ans;
        ans.reserve(n - k + 1);
        long long windowSum = 0;
        unordered_map<int,int> count;
        multiset<pair<int,int>> top;  // (freq, value)
        multiset<pair<int,int>> bot;

        auto update = [&](int num, int delta) {
            int old = count[num];
            if (old > 0) {
                auto it = bot.find({old, num});
                if (it != bot.end()) {
                    bot.erase(it);
                } else {
                    it = top.find({old, num});
                    top.erase(it);
                    windowSum -= (long)num * old;
                }
            }
            int nw = old + delta;
            if (nw > 0) {
                count[num] = nw;
                bot.insert({nw, num});
            } else {
                count.erase(num);
            }
        };

        for (int i = 0; i < n; ++i) {
            update(nums[i], +1);
            if (i >= k) {
                update(nums[i - k], -1);
            }
            while (!bot.empty() && (int)top.size() < x) {
                auto it = prev(bot.end());
                auto p = *it;
                bot.erase(it);
                top.insert(p);
                windowSum += (long)p.second * p.first;
            }
            while (!bot.empty() && !top.empty()) {
                auto b = *prev(bot.end());
                auto t = *top.begin();
                if (b.first > t.first || (b.first == t.first && b.second > t.second)) {
                    bot.erase(prev(bot.end()));
                    top.erase(top.begin());
                    bot.insert(t);
                    top.insert(b);
                    windowSum += (long)b.second * b.first;
                    windowSum -= (long)t.second * t.first;
                } else {
                    break;
                }
            }
            if (i >= k - 1) {
                ans.push_back(windowSum);
            }
        }
        return ans;
    }
};
