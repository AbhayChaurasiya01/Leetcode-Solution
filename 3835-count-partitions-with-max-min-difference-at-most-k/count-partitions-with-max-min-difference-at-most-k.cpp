class Solution {
public:
    int countPartitions(vector<int>& nums, int k) {
        const int MOD = 1'000'000'007;
        int n = nums.size();

        vector<int> dp(n + 1, 0), pref(n + 1, 0);
        dp[0] = 1;
        pref[0] = 1;

        deque<int> maxdq, mindq;
        int l = 0;

        for (int r = 0; r < n; r++) {

            // maintain max deque
            while (!maxdq.empty() && nums[maxdq.back()] <= nums[r])
                maxdq.pop_back();
            maxdq.push_back(r);

            // maintain min deque
            while (!mindq.empty() && nums[mindq.back()] >= nums[r])
                mindq.pop_back();
            mindq.push_back(r);

            // adjust left pointer until valid window
            while (l <= r && nums[maxdq.front()] - nums[mindq.front()] > k) {
                if (maxdq.front() == l) maxdq.pop_front();
                if (mindq.front() == l) mindq.pop_front();
                l++;
            }

            long long sum = pref[r] - (l - 1 >= 0 ? pref[l - 1] : 0);
            sum = (sum % MOD + MOD) % MOD;

            dp[r + 1] = sum;
            pref[r + 1] = (pref[r] + dp[r + 1]) % MOD;
        }

        return dp[n];
    }
};
