class Solution {
public:
    std::vector<int> maximumWeight(std::vector<std::vector<int>>& intervals) {
        int n = intervals.size();
        for (int i = 0; i < n; ++i) {
            intervals[i].push_back(i);
        }

        // Sort by end time
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& left, const std::vector<int>& right) {
            return left[1] < right[1];
        });

        std::vector<std::vector<std::pair<long, std::vector<int>>>> dp(n, std::vector<std::pair<long, std::vector<int>>>(5, {0, {}}));

        dp[0][1] = { intervals[0][2], { intervals[0][3] } };
        long maxWeight = intervals[0][2];

        for (int i = 1; i < n; ++i) {
            int low = 0, high = i - 1, idx = -1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (intervals[mid][1] < intervals[i][0]) {
                    idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }

            for (int j = 1; j < 5; ++j) {
                dp[i][j] = dp[i - 1][j]; // Inherit from previous state
                if (idx != -1) {
                    long newWeight = dp[idx][j - 1].first + intervals[i][2];
                    std::vector<int> newIndices = dp[idx][j - 1].second;
                    newIndices.push_back(intervals[i][3]);
                    std::sort(newIndices.begin(), newIndices.end());

                    if (dp[i][j].first < newWeight || (dp[i][j].first == newWeight && newIndices < dp[i][j].second)) {
                        dp[i][j] = { newWeight, newIndices };
                    }
                }

                if (j == 1) {
                    long singleWeight = intervals[i][2];
                    std::vector<int> singleIndex = { intervals[i][3] };

                    if (dp[i][j].first < singleWeight || (dp[i][j].first == singleWeight && singleIndex < dp[i][j].second)) {
                        dp[i][j] = { singleWeight, singleIndex };
                    }
                }

                maxWeight = std::max(maxWeight, dp[i][j].first);
            }
        }

        std::vector<int> result = { 100000 };
        for (int j = 1; j < 5; ++j) {
            if (maxWeight == dp[n - 1][j].first) {
                result = std::min(result, dp[n - 1][j].second);
            }
        }

        return result;
    }
};